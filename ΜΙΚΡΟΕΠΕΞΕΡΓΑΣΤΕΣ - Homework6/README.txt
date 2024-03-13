Γιάτσος Γεώργιος - ΑΜ:3202

Για τη διευκόλυνσή σας και τη σωστή λειτουργία των testbench των ερωτημάτων της άσκησης, ακολουθεί το παρακάτω κείμενο.

Όλα τα αρχεία του project είναι συγκεντρωμένα στο φάκελο "project files".

Για το πρώτο ερώτημα και το πρώτο σκέλος υλοποιήθηκε καταλλήλως το αρχείο "alutb.v", ενώ για το δεύτερο σκέλος το "alu1tb.v" 
Για το δεύτερο ερώτημα και το πρώτο και δεύτερο σκέλος δημιουργήθηκαν τα αρχεία "ramcontrollertb.v" και "ramcontrollertbam.v" αντιστοίχως.
Για το τρίτο ερώτημα τροποποιήθηκαν τα αρχεία "cpu.v", "cputb.v", "cputbam.v" και "registerfile.v".
Ωστόσο, χρησιμοποιώ το αρχείο "cputbam.v" και για την υλοποίηση του 4ου ερωτήματος.
Για το πέμπτο ερώτημα υλοποίησα τα αρχεία "helistonetb.v" και "heilstonetbam.v".

Σε κάθε φάκελο για κάθε ένα ερώτημα ξεχωριστά βρίσκονται και τα απαραίτητα αρχεία καθώς και οι κυματομορφές σε τύπο .png με "a" για το πρώτο σκέλος και "b" για το δεύτερο σκέλος.

Το compile order είναι το εξής:
ramcontroller.v
ramcontrollertb.v
ramcontrollertbam.v
registerfile.v
alu.v
alutb.v
alu1tb.v
cpu.v
cputb.v
cputbam.v
heilstonetb.v
heilstonetbam.v
Προσπάθησα να το κρατήσω όσο το δυνατόν πιο κοντά σε αυτό που μας υποδείξατε.

Τέλος, για το ποιο testbench θα τρέξετε σε κάθε σκέλος διαβάστε την εξής αντιστοίχιση:
1α->alutb.v
1b->alu1tb.v
2a->ramcontrollertb.v
2b->ramcontrollertbam.v
3a->cputb.v
3b->cputbam.v
4 ->cputbam.v
5a->heilstonetb.v
5b->heilstonetbam.v










