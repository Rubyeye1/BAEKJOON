#include <stdio.h>

int main(void)
{
	int King = 0;
	int Queen = 0;
	int Rook = 0;
	int Bishop = 0;
	int Knight = 0;
	int Pawn = 0;

	scanf("%d %d %d %d %d %d", &King, &Queen, &Rook, &Bishop, &Knight, &Pawn);
	printf("%d %d %d %d %d %d", 1 - King , 1 - Queen, 2 - Rook, 2 - Bishop , 2 - Knight , 8 - Pawn );



	return 0;
}