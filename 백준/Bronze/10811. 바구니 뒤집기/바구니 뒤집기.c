#include <stdio.h>
void swap(int *,int *);
int main(){
  int n,m,a,b;
  int num[100];
  scanf("%d %d",&n,&m);
  for(int i=0;i<n;i++){
    num[i]=i+1;
  }
  for(int i=0; i<m;i++){
    scanf("%d %d",&a,&b);
    for(a;a<b+1;a++,b--){
      swap(&num[a-1],&num[b-1]);
    }
  }
  for(int i=0; i<n;i++){
    printf("%d ",num[i]);
  }
}
void swap(int *a, int *b){
  int temp = 0;
  temp=*a;
  *a=*b;
  *b=temp;
}