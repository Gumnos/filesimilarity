# filesimilarity 0.1
Takes a series of files and reports them grouped by similar word-triad counts

## Usage

  $ ./similar.py file1.txt file2.txt file3.txt

returns groupings of files prefixed by the count of word-triads they share.
The higher the count/score, the more likely the files are the same
or share the same source.

    $ ls carroll* doyle*holmes*
    carroll_alice_in_wonderland.txt
    carroll_through_the_looking_glass.txt
    doyle_adventure_of_sherlock_holmes.txt
    doyle_return_of_sherlock_holmes.txt

    $ similar.py carroll* doyle*holmes*
    195:carroll_alice_in_wonderland.txt,carroll_through_the_looking_glass.txt,doyle_adventure_of_sherlock_holmes.txt
    205:carroll_alice_in_wonderland.txt,carroll_through_the_looking_glass.txt,doyle_return_of_sherlock_holmes.txt
    524:carroll_alice_in_wonderland.txt,carroll_through_the_looking_glass.txt,doyle_adventure_of_sherlock_holmes.txt,doyle_return_of_sherlock_holmes.txt
    555:carroll_alice_in_wonderland.txt,doyle_adventure_of_sherlock_holmes.txt,doyle_return_of_sherlock_holmes.txt
    597:carroll_alice_in_wonderland.txt,doyle_return_of_sherlock_holmes.txt
    614:carroll_through_the_looking_glass.txt,doyle_adventure_of_sherlock_holmes.txt,doyle_return_of_sherlock_holmes.txt
    635:carroll_alice_in_wonderland.txt,doyle_adventure_of_sherlock_holmes.txt
    703:carroll_through_the_looking_glass.txt,doyle_adventure_of_sherlock_holmes.txt
    756:carroll_through_the_looking_glass.txt,doyle_return_of_sherlock_holmes.txt
    1240:carroll_alice_in_wonderland.txt,carroll_through_the_looking_glass.txt
    8214:doyle_adventure_of_sherlock_holmes.txt,doyle_return_of_sherlock_holmes.txt

The output indicates that Doyle's
_Adventure of Sherlock Holmes_
and
_Return of Sherlock Holmes_
are similar, sharing 8214 word-triads in common.
Likewise, Lewis Carroll's
_Alice in Wonderland_
and
_Through the Looking Glass_
are most similar to each other,
sharing 1240 word-triads between them.

## TODO

I'd still like to have the output be a bit more sensible,
returning top matches by file,
rather than every permutation of files
if they share any common word-triads.
