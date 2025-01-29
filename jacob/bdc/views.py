from django.shortcuts import render
from django.template.loader import render_to_string
from django.templatetags.static import static


# Create your views here.
def index(request):
    return render(request, 'bdc_home.html')

def exchange(request):
    context = {
        'header_img': static("bdc-exchange-rates.jpg"),
        'service': "Exchange",
        'info_img': static("bdc-notes-rolled.png"),
        'info': render_to_string("partials/service_info_exchange.html"),
    }
    print(context)
    return render(request, "bdc_service.html", context=context)

def transfer(request):
    context = {
        'header_img': static("bdc-transfer-2.jpg"),
        'service': "Transfer",
        'info_img': static("bdc-transfer-1.jpg"),
        'info': render_to_string("partials/service_info_general.html", context={
            "title": "International Money Transfers",
            "info": """
            Fast, Secure, and Reliable International Money Transfers for Individuals and Businesses

            At Aventro Bureau de Change, we specialize in making international money transfers quick, secure, and hassle-free. Whether you're an individual sending money to loved ones abroad or a business managing global transactions, we’ve got you covered. By partnering with trusted global financial institutions, we ensure that every transfer is handled with the highest level of reliability and security.

            Our services cater to both inbound and outbound remittances, offering a seamless experience for sending and receiving funds across borders. With a focus on speed and convenience, we eliminate the complexities often associated with international transfers, allowing you to focus on what matters most. 

            Choose Aventro Bureau de Change for a trusted, efficient, and secure way to move money globally. Your financial peace of mind is our priority.
            """
        }),
    }
    return render(request, "bdc_service.html", context=context)


def hedge(request):
    context = {
        'header_img': static("bdc-hedge-2.jpg"),
        'service': "Hedge",
        'info_img': static("bdc-hedge-1.jpg"),
        'info': render_to_string("partials/service_info_general.html", context={
            "title": "Hedging and Risk Management",
            "info": """
            Empowering Businesses to Navigate Currency Risks with Confidence  

            At Aventro Bureau de Change, we understand the challenges businesses face in an ever-changing global economy. Fluctuating exchange rates can significantly impact your bottom line, which is why we offer tailored solutions to help you manage currency risks effectively.  

            Our expertise lies in providing forward contracts and options, enabling you to lock in exchange rates and protect your business from unexpected market movements. Beyond these tools, we offer strategic guidance to help you identify and mitigate exposure to currency volatility, ensuring your financial stability in a dynamic marketplace.  

            To further support your decision-making, our team conducts in-depth market analysis, delivering insights into volatile currency markets. This empowers you to make informed, proactive financial decisions that align with your business goals.  

            With Aventro Bureau de Change, you gain a trusted partner dedicated to safeguarding your business against currency risks and helping you achieve long-term financial success. Let us help you turn market challenges into opportunities.

            """
        }),
    }
    return render(request, "bdc_service.html", context=context)

def travel(request):
    context = {
        'header_img': static("bdc-travel-2.jpg"),
        'service': "Travel",
        'info_img': static("bdc-travel-1.jpg"),
        'info': render_to_string("partials/service_info_general.html", context={
            "title": "Travel with Confidence: Secure, Convenient Currency Solutions",
            "info": """
            At Aventro Bureau de Change, we empower travelers and globetrotters with tools designed to simplify international journeys. Our pre-paid currency cards and traveler’s cheques provide a secure, cash-free way to manage expenses abroad, minimizing risks associated with carrying large amounts of money.

            To streamline your travel preparation, we offer currency delivery services, ensuring you have the cash you need delivered directly to your doorstep before your trip. Beyond transactions, our team provides personalized guidance on local currency requirements and exchange regulations, helping you navigate foreign financial landscapes with ease.

            Whether you’re a frequent traveler or planning a once-in-a-lifetime adventure, we equip you with the knowledge and resources to avoid surprises. From tailored advice to flexible currency solutions, we prioritize your peace of mind, so you can focus on the experiences that matter most.

            Choose Aventro Bureau de Change for effortless travel planning and financial security—because every journey deserves a seamless start.
            """
        }),
    }
    return render(request, "bdc_service.html", context=context)

def consult(request):
    context = {
        'header_img': static("bdc-consult-2.jpg"),
        'service': "Consult",
        'info_img': static("bdc-consult-1.jpg"),
        'info': render_to_string("partials/service_info_consulting.html"),
    }
    return render(request, "bdc_service.html", context=context)
