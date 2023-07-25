package quicksort;

public class QuickSort {

    // 快速排序算法
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length == 0) {
            return;
        }
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int partitionIndex = partition(arr, left, right);
            quickSort(arr, left, partitionIndex - 1);
            quickSort(arr, partitionIndex + 1, right);
        }
    }

    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[right]; // 选取最右边的元素作为基准值
        int i = left - 1; // i指向小于基准值的元素位置

        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }

        swap(arr, i + 1, right);
        return i + 1; // 返回基准值的正确位置
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = {3, 9, 2, 7, 5, 1, 8, 6, 4};
        quickSort(arr);
        System.out.println("排序后的数组：");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
    //基本思路：通过选择一个基准值（这里选取最右边的元素），
    //将数组分为左右两部分，左边部分的元素小于等于基准值，
  //右边部分的元素大于基准值。然后对左右两部分递归地进行快速排序，
   // 直到数组排序完成。最后，输出排序后的数组。运行代码后，
    //输出的结果是按照从小到大排列的数组。
}
