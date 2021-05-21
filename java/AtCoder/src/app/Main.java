package app;

import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String[] sNK = scanner.nextLine().split(" ");
        String[] sA = scanner.nextLine().split(" ");
        String[] sF = scanner.nextLine().split(" ");
        scanner.close();

        int N = Integer.parseInt(sNK[0]);
        long K = Long.parseLong(sNK[1]);

        int[] A = new int[N];
        Integer[] F = new Integer[N];
        int[] AF = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(sA[i]);
            F[i] = Integer.parseInt(sF[i]);
        }

        Arrays.sort(A);
        Arrays.sort(F, Collections.reverseOrder());
        for (int i = 0; i < N; i++) {
            AF[i] = A[i] * F[i];
        }

        Comparator<Integer> c = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return AF[o2] - AF[o1];
            }
        };

        Integer[] idx = new Integer[N];
        for (int i = 0; i < N; i++) {
            idx[i] = i;
        }
        Arrays.sort(idx, c);

        int[] tA = new int[N];
        int[] tF = new int[N];
        int[] tAF = new int[N];
        int max = AF[idx[0]];
        for (int i = 0; i < N; i++) {
            tA[i] = A[idx[i]];
            tF[i] = F[idx[i]];
            tAF[i] = AF[idx[i]];
        }

        if (func(0, tAF, tF, N, K)) {
            System.out.print(0);
            return;
        }
        int a = 0;
        int b = max;
        for (int aaa = 0; aaa < max; aaa++) {
            if ((b - a) <= 1) {
                System.out.print(b);
                return;
            }
            int mid = (int) ((b - a) / 2. + a);
            if (func(mid, tAF, tF, N, K)) {
                b = mid;
            } else {
                a = mid;
            }
        }
        System.out.print("????????");
    }

    public static boolean func(int saidai, int[] AF, int[] F, int N, long K) {
        long count = 0;
        for (int n = 0; n < N; n++) {
            if (AF[n] <= saidai) {
                return true;
            }
            count += Math.ceil((AF[n] - saidai) / ((double) F[n]));
            if (count > K) {
                return false;
            }
        }
        return true;
    }
}
