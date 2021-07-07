#include <stdlib.h>
#include <string.h>

char *dna_to_rna(const char *dna)
{
  size_t len = strlen(dna);
  char *rna = calloc(len + 1, sizeof(char));
  rna[len] = 0;
    for (int i=0; i<len; i++) {
	if (dna[i] == 'T') {
	    rna[i]='U';
	}
	else {
	    rna[i]=dna[i];
	}
    }
    return rna;
}
