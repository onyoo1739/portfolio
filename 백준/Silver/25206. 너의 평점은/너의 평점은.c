#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct credit{
  char name[51];
  float credit;
  char score[3];
}credit;
int main() {
  float sum_credit=0.0;
  float sum_score=0;
  struct credit c[20];
  for(int i=0;i<20;i++){
    scanf("%s %f %s",c[i].name,&c[i].credit,c[i].score);
  }  
  for(int i=0;i<20;i++){
    sum_credit+=c[i].credit;
    if (strcmp(c[i].score,"A+")==0){
      sum_score+=(4.5 * c[i].credit);
    }
    else if(strcmp(c[i].score,"A0")==0){
      sum_score+=(4.0 * c[i].credit);
    }
    else if(strcmp(c[i].score,"B+")==0){
      sum_score+=(3.5* c[i].credit);
    }
    else if(strcmp(c[i].score,"B0")==0){
      sum_score+=(3.0* c[i].credit);
    }
    else if(strcmp(c[i].score,"C+")==0){
      sum_score+=(2.5* c[i].credit);
    }
    else if(strcmp(c[i].score,"C0")==0){
      sum_score+=(2.0* c[i].credit);
    }
    else if(strcmp(c[i].score,"D+")==0){
      sum_score+=(1.5* c[i].credit);
    }
    else if(strcmp(c[i].score,"D0")==0){
      sum_score+=(1.0* c[i].credit);
    }
    else if(strcmp(c[i].score,"F")==0){
      sum_score+=0.0;
    }
    else if(strcmp(c[i].score,"P")==0){
      sum_credit -=c[i].credit;
    }
  }
  printf("%.6f",sum_score/sum_credit);
}