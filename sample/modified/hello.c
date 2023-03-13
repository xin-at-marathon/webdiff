
#include <stdio.h>

#ifdef FOO_001
int foobar() {
	printf("foobar");
}
endif

int main() {
	// printf() displays the string inside quotation modified
	printf("Hello");

	printf("World!");
	// added
	return 0;
}
