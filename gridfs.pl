#!/usr/bin/perl
#Author: Jeremy Eudy
#Usage: clear; perl gridfs.pl
use warnings;
use diagnostics;
use MongoDB;
use MongoDB::GridFS;
use File::Basename;
use IO::File;

my $client = MongoDB::MongoClient->new(host => 'localhost');
my $db = $client->get_database( 'SGA_Inventory' );
my $grid = $db->get_gridfs;
print "MongoDB Connected.\n";

$grid->drop();

my @lines;
my $textFile = 'SGA_Assets.txt';
open my $info, '<', $textFile or die "Could not open '$textFile': '$!'";
print "Pushing $textFile info to array...\n";
while(<$info>){
	push (@lines, $_);
}

my $photoDir = '~/Database/Photos';
my $i = 0;

foreach my $file ( <$photoDir/*> ) {
	if ( my $fh = IO::File->new($file, "r") ) {
		my $photo = basename($file);
		print "Current filename: $photo\n";
	        print "Storing file...\n";
		my($timestamp, $item, $quantity, $condition, $location, $filename, $owner) = split /\;/, $lines[$i];
		$item = uc $item; $quantity = uc $quantity; $condition = uc $condition; $location = uc $location; $owner = uc $owner;
		if ( $filename eq "$photo - Google Drive"){
			print "$timestamp\n$item\n$quantity\n$condition\n$location\n$filename\n$owner\n";
			print "------------------------------------------------------------------------\n";
			my $meta = {
				"Time Stamp" => $timestamp,
				"Item Name" => $item,
				"Quantity" => $quantity,
				"Condition" => $condition,
				"Location" => $location,
            			"File name" => $filename,
				"Owner" => $owner,
	    		    	"Content-type" => "photo/jpeg",
      		        };
	       		$grid->insert($fh, $meta);
		} else {
			print "Error: Filename Conflict.\n";
			exit;
		}
	}
	$i++;
}


exit;
