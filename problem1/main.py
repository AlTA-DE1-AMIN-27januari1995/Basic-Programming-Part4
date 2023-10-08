def play_with_asterisk(n):
    for i in range(1, n+1):
        # Mencetak spasi sebanyak n-i
        for j in range(n-i):
            print(" ", end="")
        # Mencetak asterisk sebanyak i
        for k in range(i):
            print("* ", end="")
        # Pindah ke baris baru setelah mencetak baris i
        print()

print(play_with_asterisk)

if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """
