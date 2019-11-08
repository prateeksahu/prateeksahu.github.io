#include <unistd.h>
#include <stdio.h>

void main(void)
{
    write(1, "This is a test\n", 15);
}
