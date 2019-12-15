#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include <unistd.h>
#include <string.h>
#include <time.h>

#include <wiringPi.h>
#include <lcd.h>

static int lcdHandle;

int main(int argc, char *argv[]) {
	int rows = 2, cols = 16;
	char str1[17], str2[17];
	wiringPiSetup();
	FILE *file;
	file = fopen("input.txt", "r");
	fgets(str1, 17, file);
	FILE *file2;
	file2 = fopen("input2.txt", "r");
	fgets (str2, 17, file2);
	lcdHandle = lcdInit (rows, cols, 4, 30,21, 22,23,24,25,0,0,0,0);
	lcdPosition (lcdHandle, 0, 0); lcdPuts (lcdHandle, str1);
	lcdPosition (lcdHandle, 0, 1); lcdPuts (lcdHandle, str2);
	return 0;
}
