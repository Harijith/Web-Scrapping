#include<iostream.h>
#include<conio.h>
class Railwayticketreserve
{
	char name[20];
	int age;
	char boardingpoint[35];
	char destination[30];
	char trainname[20];
	int coach;
	char berth[5];
	int clas;
	int trainno;
	int departuretime;
	public:
	void book();
	void display();
};
	void Railwayticketreserve::book()
	{
		cout<<"\n Enter your Name:";
		cin>>name;
		cout<<"\n Enter the age:";
		cin>>age;
		cout<<"\n Enter your boarding point:";
		cin>>boardingpoint;
		cout<<"\n Enter your Destination:";
		cin>>destination;
		cout<<"\n Enter the trainno.:";
		cin>>trainno;
		cout<<"\n Entet the train name:";
		cin>>trainname;
		cout<<"\n Entet the Departure time:";
		cin>>departuretime;
		cout<<"\n Enter the travel class required:";
		cin>>clas;
		cout<<"\n Enter the coach required:";
		cin>>coach;
		cout<<"\n Enter the berth required:";
		cin>>berth;

	}
	void Railwayticketreserve::display()
	{

		cout<<"\n Name: "<<name<< "\tAge: "<<age<<"\tBoarding Point: "<<boardingpoint<<"\tDestination: "<<destination<<"\tTrain No.: "<<trainno<<"\tTrain Name: "<<trainname<<"\tDeparture Time: "<<departuretime<<"\tClass: "<<clas<<"\tCoach: "<<coach<<"\tBerth: "<<berth;
		cout<<"\n-----------------------------------------------------------";
	}
void main()
{
	int n,N=500;
	clrscr();
	cout<<"\n Enter the number of tickets to be booked: ";
	cin>>n;
	Railwayticketreserve obj[50];
	for(int i=0;i<n;i++)
	{
		obj[i].book();
		cout<<"\n-----------------------------------------------------------------------";
	}
	for(i=0;i<n;i++)
	{
		obj[i].display();
		cout<<"\n-----------------------------------------------------------------------";
	}
	N=N-n;
	cout<<"\n The total no. of tickets available are:"<<N;
	getch();
}