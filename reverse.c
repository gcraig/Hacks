#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * reverse the string pointed to by character
 * pointer 's'. returns NULL if s is uninitialized.
 */
char* reverse(const char* s) 
{
	if (!s)
		return NULL;

	int i = 0, j = 0;
	int len = strlen(s);
	char* reverse_str = (char*) malloc(len);

	for (i = len-1; i > -1; i--)
	{
		reverse_str[j++] = s[i];
	}

	return reverse_str;
}

int main() 
{
	const char* s = "classic string reversal";
	puts(s);
	puts(reverse(s));
	return 0;
}