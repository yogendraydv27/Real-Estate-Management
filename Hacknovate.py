import pandas as pd
import matplotlib.pyplot as plt
print(' '*50,'WELCOME TO REAL-ESTATE')
print(' '*47,'Harit Vatika Project pvt.ltd. ')
print(' '*37,'Residential plots near jewar international Airport \n')
while True:
    a=pd.DataFrame([['Plot size according to your budget'],['Residential plots sizes'],['Facilities and Amenities of society'],['prices of residential plot'],['visualize the plot prizes and sizes'],['location of site']],columns=["[choose  the following]"],index=[1,2,3,4,5,6])
    print('\n')
    print(a,'\n')
    print('=(if you are interested then select the following)\n')
    b=int(input('Enter your choice:'))
    print('')
    if b==1:
        w=int(input('ENTER YOUR MIN. BUDGET:'))
        xy=int(input('ENTER YOUR MAX. BUDGET:'))
        pq={1250000:"100 SQ.UD.",1875000:"150 SQ.UD.",2500000:"200 SQ.UD.",3750000:"300 SQ.UD."}
        print('')
        for i in pq:
            if i>=w and i<=xy:
                print('The best plot in your budget:',pq[i])
                if pq[i]=='100 SQ.UD.':
                    print('Price:12,50,000')
                    mn=pd.DataFrame([['51000'],['250000'],['250000'],['250000'],['250000'],['199000'],['=1250000']],columns=["100 Sq.Yd"],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
                    print('Payment plan:')
                    print(mn)
                    print('#Note: BSP is Basic sale price \n')
                elif pq[i]=='150 SQ.UD.':
                    print('Price:1875000')
                    kl=pd.DataFrame([['71000'],['375000'],['375000'],['375000'],['375000'],['304000'],['=1875000']],columns=["150 Sq.Yd"],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
                    print('Payment plan:')
                    print(kl)
                    print('#Note: BSP is Basic sale price \n')
                elif pq[i]=='200 SQ.UD.':
                    print('Price:2500000')
                    op=pd.DataFrame([['91000'],['500000'],['500000'],['500000'],['500000'],['409000'],['=2500000']],columns=["200 Sq.Yd"],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
                    print('Payment plan:')
                    print(op)
                    print('#Note: BSP is Basic sale price \n')
                elif pq[i]=='300 SQ.UD.':
                    print('Price:3750000')
                    gh=pd.DataFrame([['111000'],['750000'],['750000'],['750000'],['750000'],['639000'],['=3750000']],columns=["300 Sq.Yd"],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
                    print('Payment plan:')
                    print(gh)
                    print('#Note: BSP is Basic sale price \n')
    elif b==2:
        c=pd.DataFrame([['100 SQ.YD. ,LENGTH=30FT,BREADTH=30FT'],['100 SQ.YD. ,LENGTH=45FT,BREADTH=20FT'],['150 SQ.YD. ,LENGTH=45FT,BREADTH=30FT'],['200 SQ.YD. ,LENGTH=45FT,BREADTH=40FT'],['200 SQ.YD. ,LENGTH=60FT,BREADTH=30FT'],['300 SQ.YD. ,LENGTH=60FT,BREADTH=45FT']],columns=["Residential plot sizes"],index=[1,2,3,4,5,6])
        print(c)
        print('#Note: 1SQ.UD.=0.836 SQ.MTR. & 1SQ.YD.=9 SQ.FT. \n')
        print('=(if you are interested then type "Prices" for plots price detail)')
        d=input(':')
        print('')
        if d=='prices' or d=='PRICES' or d=='Prices':
            e=pd.DataFrame([['1250000'],['1875000'],['2500000'],['3750000']],columns=['PRICE'],index=['(1) 100 SQ.YD.:-','(2) 150 SQ.YD.:-','(3) 200 SQ.YD.:-','(4) 300 SQ.YD.:-'])
            print(e,'\n')
            print('=(if you are interested to know about PAYMENT PLAN then type "plan")')
            f=input(':')
            print('')
            if f=='plan' or f=='PLAN':
                g=pd.DataFrame([["51,000","71,000","91,000","1,11,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["1,99,000","3,04,000","4,09,000","6,39,000"],['=12,50,000','=18,75,000','=25,00,000','=37,50,000']],columns=["100 SQ.YD.","150 SQ.YD.","200 SQ.YD.","300 SQ.YD."],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
                print('                                                             (BSP=12500/Sq.Yd.)')
                print(g)
                print('#Note: BSP is Basic sale price \n')
                check=input("Do you want to continue? yes/no:")
                if check=="no" or check=="NO" or check=="No":
                    break
    elif b==3:
        k=pd.DataFrame(["street light","wide Road","24x7 Security","parks","Community Centre","Water supply","gated and walled society","commercial Area","Drainage symtem","Electricity Facilities"],columns=["FACILITIES AND AMENTIES OF SOCIETY"],index=["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)","(10)"])
        print(k,"\n")
        check=input("Do you want to continue? yes/no:")
        if check=="no" or check=="NO" or check=="No":
            break
    elif b==4:
        h=pd.DataFrame([["12,50,000"],["18,75,000"],["25,00,000"],["37,50,000"]],columns=["price"],index=["(1) 100 SQ.YD","(2) 150 SQ.YD","(3) 200 SQ.YD","(4) 300 SQ.YD"])
        print(h, "\n")
        print("=(if you are interested to know about PAYMENT PLAN the type 'plan')")
        m=input(":")
        print("\n")
        if m=="plan" or m=="PLAN":
              v=pd.DataFrame([["51,000","71,000","91,000","1,11,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["2,50,000","3,75,000","5,00,000","7,50,000"],["1,99,000","3,04,000","4,09,000","6,39,000"],['=12,50,000','=18,75,000','=25,00,000','=37,50,000']],columns=["100 SQ.YD.","150 SQ.YD.","200 SQ.YD.","300 SQ.YD."],index=["BOOKING AMOUNT","within 30 days from booking","within 60 days from booking","within 90 days from booking","within 120 days from booking","At the time of registry","Total cost(bsp)"])
              print("                                                               (bsp=12,500/sq.yd.)")
              print(v)
              print("#note: Bsp is Basic sale price \n")
              check=input("Do you want to continue? yes/no:")
              if check=="no" or check=="NO" or check=="No":
                  break
    elif b==5:
        x=["100 SQ.YD.","150 SQ.YD.","200 SQ.YD.","300 SQ.YD."]
        y=["12,50,000","18,75,000","25,00,000","37,50,000"]
        plt.plot(x,y,label='line represent the price and size of plot')
        plt.xlabel("plot sizes")
        plt.ylabel("plot prices")
        plt.title("representation of plot prize and sizes")
        plt.legend()
        plt.grid(True)
        plt.show()
        check=input("Do you want to continue? yes/no:")
        if check=="no" or check=="NO" or check=="No":
            break
    elif b==6:
        q=pd.DataFrame(['Harit Vatika Project pvt.ltd.','on yamuna Expressway','Near Jewar international Airport','Noida sector=186','uttar Pradesh=201945'],columns=["{LOCATION OF SITE}"],index=[' ',' ',' ',' ',' '])
        print(q,'\n')
        check=input("Do you want to continue? yes/no:")
        if check=="no" or check=="NO" or check=="No":
            break
    else:
        print("Enter correct input \n")
        check=input("Do you want to continue? yes/no:")
        if check=="no" or check=="NO" or check=="No":
            break

              


