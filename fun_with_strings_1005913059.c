#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
const char * pidgin(char input[]);
const char * vowel_caser(char input[]);
int main()
{
    char line[61] = "A strIng is jUst a bunch Of chArs sittIng togEthEr in A row!\0";
    printf("%s\n", line);
    printf("%s\n", pidgin(line));
    printf("%s\n", vowel_caser(line));
}

const char * pidgin(char input[])
{
    int index = 0;
    char temp;
    while(input[index] != '\0' && input[index+1] != '\0'){
        temp = input[index];
        input[index] = input[index+1];
        input[index+1] = temp;
        index = index + 2;
    }
    return input;
}

const char * vowel_caser(char input[])
{
    int index = 0;
    int lowercase, uppercase;
    while(input[index] != '\0'){
        lowercase = (input[index] == 'a' || input[index] == 'e' || input[index] == 'i' || input[index] == 'o' || input[index] == 'u');
        uppercase = (input[index] == 'A' || input[index] == 'E' || input[index] == 'I' || input[index] == 'O' || input[index] == 'U');
        if (lowercase || uppercase){
            if (isupper(input[index])){
                input[index] = tolower(input[index]);
            }
            else if (islower(input[index])){
                input[index] = toupper(input[index]);
            }
            index = index + 1;
        }
    }
    return input;
}