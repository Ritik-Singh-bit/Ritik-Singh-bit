#include<stdio.h>
#include<conio.h>
#include<string.h>

     struct book_record
    {
     int no;
     char name[20];
     float price;
     char publication[10];
     int year;
     char author[20];
    };

      void main()
   {
    struct  book_record b[5];
     clrscr();
     printf("enter book details :");
     scanf("%d",&b[0].no);
     scanf("%s",&b[0].name);
     scanf("%f",&b[0].price);
     scanf("%s",&b[0].publication);
     scanf("%d",&b[0].year);
     scanf("%s",&b[0].author);

     printbook_record(b);
     getch();
     }
      void printbook_record(struct book_record b)
      {
	printf("book record is : %d,%s,%f,%s,%d,%s\n",b.no,b.name,b.price,b.publication,b.year,b.author);
	}
