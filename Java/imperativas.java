package Java;
import java.util.List;

public class imperativas {
    
    public int soma(int n) {
        int resultado = 0;
        for (short i = 1; i <= n; i++) {
            resultado += i;
        }
        return resultado;
    }

    public int div(int m, int n) {
        int resultado = n;
        if (m > n) {
            for (int i = 0; i < m; i++) {
                if (resultado <= m) {
                    resultado += n;
                } else {
                    resultado = i;
                    break;
                }
            }
        } else {
            return 0;
        }
        return resultado;
    }

    public float media(int k) {
        int soma = 0;
        String numero = String.valueOf(k);

        if (k != 0) {
            String digitos[] = numero.split("");
            for (int i = 0; i < numero.length(); i++) {
                soma += Integer.valueOf(digitos[i]);
            }
        }
        return soma / numero.length();
    }

    public int num_it(int x) {
        int k = x;
        int i = 0;
        while (k != 1) {
        if (k % 2 == 0) {
            k = k / 2;
            i++;
        } else {
            k = 3 * k + 1;
            i++;
        }
        }
        if (k == 1) {
            return i;
        }
        return 0;
    }
}
