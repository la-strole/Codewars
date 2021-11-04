#include <stddef.h>

/* C program for Merge Sort */
#include <stdio.h>
#include <stdlib.h>
  
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
  
    /* create temp arrays */
    int L[n1], R[n2];
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
  
    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
  
    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
  
/* l is for left index and r is right index of the
sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int m = l + (r - l) / 2;
  
        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
  
        merge(arr, l, m, r);
    }
}
  

int *shuffled_array(const int *array, size_t n) {
   
    // copy original array
    int *answer_array = malloc(n * sizeof(size_t));
    if (answer_array == NULL){
        fprintf(stderr, "malloc faild\n");
    }
    
    for (int i=0; i < n; i++){
        answer_array[i] = array[i];
    }

    mergeSort(answer_array, 0 , n - 1);
    // find sum of elements
    int sum = 0;
    for (int i=0; i< n; i++){
        sum = sum + answer_array[i];
    }
    sum = sum / 2;
    // find element equal to sum in array and swap all elements to the left
    int index = 0;
    for (int i=0; i < n; i++){
        if (answer_array[i] == sum){
            index = i;
            for (;index < n - 1; index++){
                answer_array[index] = answer_array[index + 1];
            }
            break;
        }
    }    
    return answer_array;

}

/* Driver code */
int main()
{
    int arr[] = { 12, 11, 54, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
  
    printf("\nGiven array is \n");
    for (int i=0; i < arr_size; i++){
        printf("%i, ", arr[i]);
    }
    
    printf("\n\nSortes array without mistake element is \n");

    int *result_array = malloc(arr_size * sizeof(int));
    result_array = shuffled_array(arr, arr_size);
    for (int i=0; i < arr_size - 1; i++){
        printf("%i, ", result_array[i]);
    }
    
  
    
    free(result_array);
    return 0;
}


