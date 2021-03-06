# Ένα Κιλό Δεδομένων

Η ποσότητα των δεδομένων που παράγεται στον κόσμο αυξάνεται ραγδαία, και μαζί μ' αυτή και οι ανάγκες αποθήκευσης. Ήδη, τα μεγάλα υπολογιστικά κέντρα είναι μεγαλύτερα από γήπεδα ποδοσφαίρου και χρειάζονται τόσο ηλεκτρικό ρεύμα όσο και μια πόλη για να λειτουργήσουν.

Οι επιστήμονες αναζητούν νέους τρόπους αποτελεσματικής αποθήκευσης δεδομένων και μία μέθοδος που έχει ενδιαφέρον είναι η χρήση του DNA ως αποθηκευτικού μέσου. Με τη σωστή κωδικοποίηση, ένα κυβικό εκατοστό DNA μπορεί να αποθηκεύσει 10<sup>16</sup> bits δεδομένων, το οποίο σημαίνει ότι μπορούμε να αποθηκεύσουμε όλα τα δεδομένα του κόσμου σε ένα κιλό DNA.

Αλλά ποια κωδικοποίηση μπορούμε να χρησιμοποιήσουμε; Μία προσέγγιση είναι η εξής. Έστω ότι θέλουμε να κωδικοποιήσουμε ένα αρχείο:

* Παίρνουμε τα περιεχόμενα του αρχείου και τα κωδικοποιούμε με κωδικοποίηση Huffman *με βάση το τρία*. Στη συνήθη κωδικοποίηση Huffman, o κώδικας Huffman που προκύπτει κωδικοποιεί τα δεδομένα μας χρησιμοποιώντας bits, δηλάδη 0 και 1. Στην κωδικοποίηση Huffman με βάση το τρία, κωδικοποιούμε τα δεδομένα μας χρησιμοποιώντας trits, δηλαδή, 0, 1, και 2. 
* Η κωδικοποίηση Huffman με βάση το τρία λειτουργεί ακριβώς με τον ίδιο τρόπο όπως και η κωδικοποίηση Huffman με βάση το δύο, όμως όταν επεξεργαζόμαστε την ουρά προτεραιτότητας, αντί να βγάζουμε κάθε φορά δύο στοιχεία και να εισάγουμε ένα, βγάζουμε τρία στοιχεία και εισάγουμε ένα. 
* Με τον τρόπο αυτό παράγεται και πάλι ένα δένδρο, το οποίο είναι τριαδικό. Στα κλαδιά του αντί για 0 και 1 αντιστοιχούμε 0, 1, και 2. Η κωδικοποίηση Huffman προκύπτει τότε και πάλι από τα μονοπάτια από το ρίζα μέχρι κάθε φύλλο του δένδρου.
* Χρειάζεται προσοχή αν το αρχείο μας δεν έχει μονό αριθμό χαρακτήρων. Αφού κατά τη διάρκεια της επεξεργασίας της ουράς προτεραιότητας κάθε φορά βγάζουμε τρία στοιχεία και προσθέτουμε ένα, κάθε φορά το μέγεθός της μειώνεται κατά δύο. Συνεπώς για να δουλέψει ο αλγόριθμος αν το αρχείο μας δεν έχει μονό αριθμό χαρακτήρων πρέπει να προσθέσουμε ένα νοητό χαρακτήρα με συχνότητα εμφάνισης μηδέν.

Έχοντας κωδικοποιήσει το αρχείο μας με τον τριαδικό κώδικα Huffman, στη συνέχεια το κωδικοποιούμε με τις βάσεις του DNA, A (adenine), C (cytocine), G (guanine), T (thymine). Για να το κάνουμε αυτό διαβάζουμε χαρακτήρα χαρακτήρα τα trits του κωδικοποιημένου με τον τριαδικό κώδικα Huffman αρχείο και κωδικοποιούμε χρησιμοποιώντας τον παρακάτω πίνακα:

<table>
  <tr>
    <th>προηγούμενη βάση</th>
    <th colspan="3">τρέχον trit</th>
  </tr>
  <tr>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>C</td>
    <td>G</td>
    <td>T</td>
  </tr>
  <tr>
    <td>C</td>
    <td>G</td>
    <td>T</td>
    <td>A</td>
  </tr>
  <tr>
    <td>G</td>
    <td>T</td>
    <td>A</td>
    <td>C</td>
  </tr>
  <tr>
    <td>T</td>
    <td>A</td>
    <td>C</td>
    <td>G</td>
  </tr>
</table>

Ο πίνακας αυτός χρησιμοποιείται ως εξής: αν θέλουμε να κωδικοποιήσουμε το trit 2 και το προηγούμενο trit που κωδικοποιήσαμε κωδικοποιήθηκε με τη βάση G, τότε το 2 θα κωδικοποιηθεί με τη βάση C, κ.ο.κ. Για το πρώτο trit, όπου δεν έχουμε κάποιο προηγούμενο, θεωρούμε ότι υπήρχε ένα νοητό προηγούμενο trit που κωδικοποιήθηκε με τη βάση A.

Για παράδειγμα, αν θέλουμε να κωδικοποιήσουμε ένα αρχείο το οποίο περιέχει τη φράση "hello, world" με τριαδικό κώδικα Huffman, θα προκύψει η παρακάτω κωδικοποίηση:

<img src="hello_world.png">

Προσέξτε ότι το αρχείο τελειώνει σε χαρακτήρα νέας γραμμής (`\n`), ο οποίος επίσης κωδικοποιείται. Επίσης, το αρχείο έχει μονό αριθμό χαρακτήρων, οπότε στην είσοδο του αλγορίθμου για την κωδικοποίηση Huffman προσθέσαμε έναν νοητό χαρακτήρα, τον οποίο συμβολίζουμε με &Oslash;. Στην πράξη, ο χαρακτήρας αυτός μπορεί να είναι απλώς ο κενός χαρακτήρας `''`, ο οποίος είναι το τίποτε, όχι ο χαρακτήρας του διαστήματος `' '`. Τον ίδιο το χαρακτήρα του διαστήματος τον συμβολίζουμε με &#9251;. Το δένδρο αυτό είναι στην ουσία ο παρακάτω πίνακας αντιστοίχισης:

| Γράμμα | Κωδικοποίηση |
|--------|--------------|
|   l    |      1       |
|   h    |     00       |
|   r    |     01       |
|   w    |     02       |
|   o    |     21       |
|&Oslash;|    200       |
|  \n    |    201       |
|&#9251; |    202       |
|   ,    |    220       |
|   d    |    221       |
|   e    |    222       |

Έτσι, η κωδικοποίηση σε τριαδικό κώδικα Huffman του αρχείου με τη φράση "hello, world" είναι η:

```
0022211212202020221011221201
```

Τώρα, εργαζόμενοι με τον πίνακα αντιστοίχισης trits και βάσεων, το `0` θα γίνει `C`, στη συνέχεια το δεύτερο `0` θα γίνει `G`, το `2` θα γίνει `C`, κ.λπ., ώστε στο τέλος θα έχουμε την παρακάτω αλυσίδα DNA:

```
CGCATCTGATGTGTGTGCTAGATGATAG
```
Η αποκωδικοποίηση αυτής της αλυσίδας DNA προχωράει με τον ακριβώς αντίστροφο τρόπο. Παίρνουμε μία-μία τις βάσεις της και τις μετατρέπουμε σε trits με βάση τον ακόλουθο πίνακα:

<table>
  <tr>
    <th>πρoηγούμενη βάση</th>
    <th colspan="4">τρέχουσα βάση</th>
  </tr>
  <tr>
    <td></td>
    <td>A</td>
    <td>C</td>
    <td>G</td>
    <td>T</td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
  </tr>
  <tr>
    <td>C</td>
    <td>2</td>
    <td></td>
    <td>0</td>
    <td>1</td>
  </tr>
  <tr>
    <td>G</td>
    <td>1</td>
    <td>2</td>
    <td></td>
    <td>0</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td></td>
  </tr>
</table>

Ο πίνακας χρησιμοποιείται όπως και στην κωδικοποίηση. Αρχικά θεωρούμε ότι η προηγούμενη βάση που έχουμε δει είναι η `A`. Στο παράδειγμά μας, παίρνουμε τη βάση `C`, η οποία αποκωδικοποιείται σε `0`. Στη συνέχεια παίρνουμε τη βάση `G`, η προηγούμενη βάση είναι η `C`, οπότε αποκωδικοποιείται σε `0`, κ.ο.κ. 

Τα trits που παράγονται τα μετατρέπουμε στα αρχικά περιεχόμενα του αρχείου με βάση τον κώδικα Huffman που κατασκευάστηκε κατά την κωδικοποίηση. Έτσι, το `00` μετατρέπεται σε `h`, το `222` μετατρέπεται σε `e`, κ.ο.κ.

## Απαιτήσεις Προγράμματος

Κάθε φοιτητής θα εργαστεί στο προσωπικό του αποθετήριο στο GitHub. Για να αξιολογηθεί μια εργασία θα πρέπει να πληροί τις παρακάτω προϋποθέσεις:

1. Όλη η εργασία θα πρέπει να βρίσκεται σε έναν κατάλογο `assignment-2016-4` μέσα στο αποθετήριο του φοιτητή.
2. Το πρόγραμμα θα πρέπει να έχει όνομα `dna_store.py`.
3. Εννοείται ότι δεν επιτρέπεται η χρήση έτοιμων βιβλιοθηκών γράφων ή τυχόν έτοιμων υλοποιήσεων των αλγορίθμων, ή τμημάτων αυτών, εκτός των βιβλιοθήκων `argparse` και `csv` της Python.
4. Θα πρέπει να υλοποιήσετε εσείς οι ίδιοι την ουρά προτεραιότητας που θα χρησιμοποιήσετε.
5. Το πρόγραμμα θα μπορεί να καλείται ως εξής:
```
python dna_store.py [-d] input output huffman
```

Σε περίπτωση που δεν δίνεται η παράμετρος `-d`, το πρόγραμμα θα διαβάζει το αρχείο που δίνεται από την παράμετρο `input` (αυτό δεν σημαίνει ότι το αρχείο ονομάζεται ντε και καλά `input`, ο χρήστης μπορεί να δίνει οποιοδήποτε όνομα), αποθηκεύει την κωδικοποίηση DNA στο αρχείο που δίνεται από την παράμετρο `output`, ενώ αποθηκεύει τον κώδικα Huffman που δημιουργήθηκε στο αρχείο που δίνεται από την παράμετρο `huffman`. Ο κώδικας Huffman θα αποθηκεύεται σε αρχείο μορφής Comma Separated Values (CSV). Για την ανάγνωση και αποθήκευση αυτών των αρχείων καλό είναι να χρησιμοποιήσετε τη βιβλιοθήκη [CSV](https://docs.python.org/3/library/csv.html).

Σε περίπτωση που δίνεται η παράμετρος `-d`, το πρόγραμμα θα διαβάζει το αρχείο που δίνεται από την παράμετρο `input`, το αποκωδικοποιεί χρησιμοποιώντας τον κώδικα Huffman που δίνεται από την παράμετρο `huffman`, και αποθηκεύει το αποκωδικοποιημένο αποτέλεσμα στο αρχείο που δίνεται από την παράμετρο `output`. Υπενθυμίζουμε ότι ένα κωδικοποιημένο αρχείο μπορεί να αποκωδικοποιηθεί μόνο με τον κώδικα Huffman που παράχθηκε στην κωδικοποίησή του.

## Παραδείγματα Εκτέλεσης

* Αν δώσετε ως είσοδο:
```
python dna_store.py hello_world.txt hello_world_dna.txt hello_world_huffman.csv
```
με το αρχείο [hello_world.txt](hello_world.txt), τότε ο κώδικας Huffman θα αποθηκευτεί στο αρχείο [hello_world_huffman.csv](hello_world_huffman.csv) και το κωδικοποιημένο αρχείο θα είναι το [hello_world_dna.txt](hello_world_dna.txt). Για να δείτε ακριβώς τα περιεχόμενα του [hello_world_huffman.csv](hello_world_huffman.csv) θα πρέπει να το κατεβάσετε στον υπολογιστή σας και να το ανοίξετε με έναν καλό editor.

* Αν δώσετε ως είσοδο:
```
python dna_store.py -d hello_world_dna.txt hello_world_decoded.txt hello_world_huffman.csv
```
το αρχείο `hello_world_decoded.txt` θα πρέπει να είναι ακριβώς το ίδιο με το αρχείο `hello_world.txt`.

* Αν δώσετε ως είσοδο:
```
python dna_store.py 1984.txt 1984_dna.txt 1984_huffman.csv
```
με το αρχείο [1984.txt](1984.txt), τότε ο κώδικας Huffman θα αποθηκευτεί στο αρχείο [1984_huffman.csv](1984_huffman.csv) και το κωδικοποιημένο αρχείο θα είναι το [1984_dna.txt](1984_dna.txt).

* Αν δώσετε ως είσοδο:
```
python dna_store.py -d 1984_dna.txt 1984_decoded.txt 1984_huffman.csv
```
το αρχείο `1984_decoded.txt` θα πρέπει να είναι ακριβώς το ίδιο με το αρχείο `1984.txt`.

## Έλεγχος Αποτελεσμάτων

Αναλόγως με τον τρόπο που θα υλοποιήσετε την ουρά προτεραιότητας και την κωδικοποίηση Huffman, ο κώδικας Huffman μπορεί να διαφέρει από αυτόν που βλέπετε στα παραδείγματα, όπως μπορεί να διαφέρουν και τα αρχεία CSV. Αυτό δεν πειράζει. Σε κάθε περίπτωση, αν το πρόγραμμά σας είναι σωστό θα πρέπει η αποκωδικοποίηση ενός αρχείου να είναι ακριβώς η ίδια με το αρχικό αρχείο.

# Περισσότερες Πληροφορίες

* Andy Extance, How DNA could store all the world’s data, Nature, Vol. 537, no. 7618, pp. 22-24, August 31, 2016. (http://www.nature.com/news/how-dna-could-store-all-the-world-s-data-1.20496)
* Nick Goldman,	Paul Bertone,	Siyuan Chen,	Christophe Dessimoz,	Emily M. LeProust, Botond Sipos and Ewan Birney, Towards practical, high-capacity, low-maintenance information storage in synthesized DNA, Nature, Vol. 494, no. 7435, pp. 77-80, February 3, 2013. (http://www.nature.com/nature/journal/v494/n7435/abs/nature11875.html) 
