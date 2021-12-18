#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

struct interval
{
    int debut;
    int fin;
    struct interval* prec;
    struct interval* suivant;
};

struct interval* new_inter(int debut, int fin)
{
    struct interval* inter = malloc(sizeof(struct interval));
    inter->debut = debut;
    inter->fin = fin;
    inter->prec = NULL;
    inter->suivant = NULL;

    return inter;
}

void diviser(struct interval* inter, int d, int f)
{
    fprintf(stderr, "Diviser [%i, %i] avec [%i, %i]\n", inter->debut, inter->fin, d, f);
    if (inter == NULL)
    {
        return;
    }

    if (f <= inter->debut)
    {
        fprintf(stderr, "\t%i est avant [%i, %i]\n", f, inter->debut, inter->fin);
        return;
    }

    if (d < inter->debut)
    {
        d = inter->debut;
    }

    if (d > inter->fin) // inter->debut < inter->fin < d < f
    {
        // On passe à l'interval suivant
        if (inter->suivant != NULL)
        {
            diviser(inter->suivant, d, f);
        }
        return;
    }
    else if (f < inter->debut)
    {
        return;
    }
    // On supprime l'intervalle en entier
    if (d == inter->debut && f == inter->fin)
    {
        inter->debut = inter->fin;
        return;
    }

    struct interval* new_next = NULL;

    int old_f = inter->fin;

    // On vérifie si l'intervalle à peindre est compris dans notre interval
    if (d >= inter->debut && f <= inter->fin)
    {
        // On vérifie si on doit créer un nouvel interval
        if (f != inter->fin)
        {
            fprintf(stderr, "\tCréer [%i, %i]\n", f, old_f);
            new_next = new_inter(f, old_f);
            new_next->suivant = inter->suivant;
            inter->suivant = new_next;
            new_next->prec = inter;
        }
    }

    inter->fin = d;
    fprintf(stderr, "\tNouvelle fin = %i\n", d);
    if (inter->debut == inter->fin)
    {

    }

    if (inter->suivant != NULL)
    {
        diviser(inter->suivant, d, f);
    }
}

int afficher(struct interval* inter)
{
    if (inter == NULL)
    {
        return 0;
    }

    int result = 0;

    if (inter->debut != inter->fin)
    {
        printf("%i %i\n", inter->debut, inter->fin);
        result = 1;
    }

    int result_next = afficher(inter->suivant);

    if (result_next == 1)
    {
        return 1;
    }
    else {
        return result;
    }
}

int main()
{
    int L;
    scanf("%d", &L);
    fprintf(stderr, "%i\n", L);

    struct interval* premier_inter = new_inter(0, L);

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int st;
        int ed;
        scanf("%d%d", &st, &ed);

        diviser(premier_inter, st, ed);
    }

    int result = afficher(premier_inter);
    if (result == 0)
    {
        printf("All painted");
    }
    return 0;
}