#include <stdio.h>

void sub1();
void sub2();
void sub3();
void sub4();

int main() {
   sub1();
   sub2();
   sub3();
   sub4();
 return 0;
}

void sub1() {
}

void sub2() {

	printf("집가고싶다\n");

}

void sub3() {
 printf("Hello World\n!");
 for (int i =1; i<10; i++){
  for (int j =1; j<10; j++){
   printf("%d * %d = %d", i, j, i*j);
  }
 }
}

void sub4() {
	printf("16학번 이지훈 입니다.");
}
