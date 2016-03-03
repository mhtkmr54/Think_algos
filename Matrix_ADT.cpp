//ADD
matrixType MatrixADT::add(matrixType M1, matrixType M2){

    int i,j;
for (i=0;i<M1.matDimension;i++)
for (j=0; j<M1.matDimension;j++){
resultMatrix.matValues[i][j] =
M1.matValues[i][j]+M2.matValues[i][j];
}
return resultMatrix;
}
//SUBTRACT
matrixType MatrixADT::subtract(matrixType M1, matrixType M2){
        int i,j;
for (i=0;i<M1.matDimension;i++)
for (j=0; j<M1.matDimension;j++){
resultMatrix.matValues[i][j] = M1.matValues[i][j]-
M2.matValues[i][j];
}
return resultMatrix;
}
//MULTIPLY
matrixType MatrixADT::multiply(matrixType M1, matrixType M2){
   int i,j,k;
for (i=0;i<M1.matDimension;i++)
for (j=0; j<M1.matDimension;j++){
resultMatrix.matValues[i][j] = 0;
}


//#include <stdio.h>
Stack returnStackWithNearestGreater(Stack inputStack)
{
  int a,i,k;
  int arr[100];
  //printf("stack to be init");
  Stack toreturn;
  int neg = -1;
  toreturn.push(neg);
  while (inputStack.pop() != -1){
     i = 0;
    arr[i] = inputStack.pop();
    i++;
  }
  int length = i;
  int c = i-2;
  while (c != 0){
    for (k = c+1 ;k < length;k++ ){
      if (arr[c] < arr[k]){
           toreturn.push(arr[k]);
           break;
      }
      toreturn.push(neg); 

     }
      c = c -1;
    }
   //printf("to be return oh yeahhh");
   return toreturn;
}
for (i=0;i<M1.matDimension;i++)
for (j=0; j<M1.matDimension;j++)
for (k=0;k<M1.matDimension;k++){
resultMatrix.matValues[i][j] =
resultMatrix.matValues[i][j]+M1.matValues[i][k]*M2.matValues[k][j];
}
return resultMatrix;
}
