int singleNumber(int* nums, int numsSize){
 int x = 0;
 int i = 0;
 for (i = 0; i<numsSize;i++)
 {
   x=x^nums[i];
 }
 return x;
}
