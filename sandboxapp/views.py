from django import views
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.db.models import Q

from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        email = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=email, password=password)
        if user is not None:
            request.session["email"] = email
            if user.is_active:
                if user.is_superuser:
                    return redirect("/adminHome")
                elif user.is_staff:
                    ins = Investors.objects.get(email=email)
                    request.session["id"] = ins.id
                    return redirect("/inHome")
                else:
                    sf = Startupfounder.objects.get(email=email)
                    request.session["id"] = sf.id
                    return redirect("/sfHome")
            else:
                msg = "Account is not Active..."
                return render(request, "login.html", {"msg": msg})
        else:
            msg = "User Dosent Exists..."
            return render(request, "login.html", {"msg": msg})
    else:
        return render(request, "login.html")


def inReg(request):
    flag = 0
    msg = ""
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]
        img = request.FILES["file"]
        # fs = FileSystemStorage()
        # filename = fs.save(img.name, img)
        # uploaded_file_url = fs.url(filename)

        if User.objects.filter(username=email).exists():
            msg = "Email already exists..."
        else:
            user = User.objects.create_user(
                username=email, password=password, is_staff=1, is_active=0
            )
            user.save()
            inv = Investors.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                document=img,
                user=user,
            )
            inv.save()
            msg = "Registration Successful..."
            flag = 1

    return render(request, "inReg.html", {"msg": msg, "flag": flag})


def sfReg(request):
    flag = 0
    msg = ""
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]
        img = request.FILES["file"]

        if User.objects.filter(username=email).exists():
            msg = "Email already exists..."

        else:
            user = User.objects.create_user(
                username=email, password=password, is_active=0
            )
            user.save()
            sf = Startupfounder.objects.create(
                name=name,
                email=email,
                phone=phone,
                address=address,
                document=img,
                user=user,
            )
            sf.save()
            msg = "Registration Successful..."
            flag = 1

    return render(request, "sfReg.html", {"msg": msg, "flag": flag})


# -----------------Admin#-----------------


def adminHome(request):
    return render(request, "adminHome.html")


def adminInvestor(request):
    data = Investors.objects.filter(user__is_active=0)
    dataActive = Investors.objects.filter(user__is_active=1)
    return render(
        request, "adminInvestor.html", {"data": data, "dataActive": dataActive}
    )


def approveInvestors(request):
    id = request.GET["id"]
    status = request.GET["status"]
    ins = User.objects.get(id=id)
    ins.is_active = status
    ins.save()
    return redirect("/adminInvestor")


def adminStartUp(request):
    data = Startupfounder.objects.filter(user__is_active=0)
    dataActive = Startupfounder.objects.filter(user__is_active=1)
    return render(
        request, "adminStartup.html", {"data": data, "dataActive": dataActive}
    )


def approveStartUp(request):
    id = request.GET["id"]
    status = request.GET["status"]
    sf = User.objects.get(id=id)
    sf.is_active = status
    sf.save()
    return redirect("/adminStartUp")


def adminViewFeedback(request):
    data = Feedback.objects.all()
    return render(request, "adminViewFeedback.html", {"data": data})


def addWorkSpace(request):
    data = WorkSpace.objects.all()
    if request.POST:
        area = request.POST["area"]
        address = request.POST["address"]
        price = request.POST["price"]
        description = request.POST["desc"]
        image = request.FILES["file"]

        addSpace = WorkSpace(
            location=address,
            size=area,
            price=price,
            description=description,
            image=image,
        )
        addSpace.save()
        messages.success(request, "Added Successfully")
        return redirect("/addWorkSpace")
    return render(request, "addWorkSpace.html", {"data": data})


def deleteWorkSpace(request):
    id = request.GET["id"]
    deleteData = WorkSpace.objects.get(id=id).delete()
    messages.success(request, "Deleted")
    return redirect("/addWorkSpace")


def updateWorkSpace(request):
    id = request.GET["id"]
    data = WorkSpace.objects.get(id=id)
    if request.POST:
        area = request.POST["area"]
        address = request.POST["address"]
        price = request.POST["price"]
        description = request.POST["desc"]
        image = request.FILES["file"]

        updateData = WorkSpace.objects.get(id=id)
        updateData.location = address
        updateData.size = area
        updateData.price = price
        updateData.description = description
        updateData.image = image
        updateData.save()

        messages.success(request, "Data Updated")
        return redirect("/addWorkSpace")
    return render(request, "updateWorkSpace.html", {"data": data})


def adminviewBookings(request):
    data = WorkSpace.objects.exclude(status="Free")
    return render(request, "adminviewBookings.html", {"data": data})


# -----------------------Investor------------------------


def inHome(request):
    id = request.session["id"]

    data = Investors.objects.get(id=id)

    post = Idea.objects.all().order_by("-id")

    if request.method == "POST":
        search = request.POST["search"]
        post = Idea.objects.filter(idea__contains=search)

    return render(request, "inHome.html", {"data": data, "post": post})


def inProfile(request):
    id = request.session["id"]
    data = Investors.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]
        proUp = Investors.objects.get(id=id)
        proUp.name = name
        proUp.email = email
        proUp.phone = phone
        proUp.address = address
        proUp.save()
        logUp = User.objects.get(username=data.user)
        logUp.set_password(password)
        logUp.username = email
        logUp.save()
        return redirect("/inHome")
    return render(request, "inProfile.html", {"data": data})


def inViewIdea(request):
    invid = request.session["id"]
    id = request.GET["post"]
    data = Idea.objects.get(id=id)
    comments = Comments.objects.filter(idea=id)
    interest = ""
    if Investmentinterest.objects.filter(investor=invid, idea=id).exists():
        interest = Investmentinterest.objects.get(investor=invid, idea=id)
    return render(
        request,
        "inViewIdea.html",
        {"data": data, "comments": comments, "interest": interest},
    )


def inShowInterest(request):
    id = request.session["id"]
    idea = request.GET["idea"]
    ida = Idea.objects.get(id=idea)
    inv = Investors.objects.get(id=id)
    db = Investmentinterest.objects.create(idea=ida, investor=inv, status="Interested")
    db.save()
    return redirect(f"/inViewIdea?post={idea}")


def inViewSf(request):
    id = request.GET["sfid"]
    cUser = request.session["id"]

    user = Startupfounder.objects.get(id=id)

    post = Idea.objects.filter(user__id=id)
    payment = 0
    viewPayment = Investmentinterest.objects.filter(investor=cUser, status="Accepted")
    for v in viewPayment:
        if int(v.idea.user.id) == int(id):
            payment = 1
    return render(
        request, "inViewSf.html", {"user": user, "post": post, "payment": payment}
    )


def inChangeImage(request):
    id = request.session["id"]
    data = Investors.objects.get(id=id)
    if request.method == "POST":
        img = request.FILES["file"]

        data.document = img
        data.save()
        return redirect("/inHome")
    return render(request, "inChangeImage.html", {"data": data})


def inViewInvestmentOffers(request):
    id = request.session["id"]
    data = Investmentinterest.objects.filter(investor=id)
    return render(request, "inViewInvestmentOffers.html", {"data": data})


def inChat(request):
    sender = request.session["email"]
    receiver = request.GET["email"]
    updateStatus = Chat.objects.filter(Q(receiver=sender) & Q(sender=receiver)).update(
        status="Seen"
    )
    if request.method == "POST":
        msg = request.POST["msg"]
        db = Chat.objects.create(sender=sender, receiver=receiver, message=msg)
        db.save()
    messages = Chat.objects.filter(
        Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender)
    )
    return render(request, "inChat.html", {"messages": messages, "user": sender})


def inMakePayment(request):
    id = request.session["id"]
    sfid = request.GET["sfid"]
    if request.method == "POST":
        amt = request.POST["amt"]
        sf = Startupfounder.objects.get(id=sfid)
        inv = Investors.objects.get(id=id)
        db = Payment.objects.create(statup=sf, investor=inv, amount=amt)
        db.save()
        return redirect("/inViewPayments")
    return render(request, "payment.html")


def inViewPayments(request):
    id = request.session["id"]
    data = Payment.objects.filter(investor=id)
    return render(request, "inViewPayments.html", {"data": data})


# -------------------------Startup Founder--------------------


def sfHome(request):
    id = request.session["id"]
    data = Startupfounder.objects.get(id=id)
    post = Idea.objects.exclude(user=id).order_by("-id")
    if request.method == "POST":
        search = request.POST["search"]
        post = Idea.objects.filter(idea__contains=search).exclude(user=id)
    return render(request, "sfHome.html", {"data": data, "post": post})


def sfProfile(request):
    id = request.session["id"]

    data = Startupfounder.objects.get(id=id)
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        password = request.POST["password"]
        proUp = Startupfounder.objects.get(id=id)
        proUp.name = name
        proUp.email = email
        proUp.phone = phone
        proUp.address = address
        proUp.save()
        logUp = User.objects.get(username=data.user)
        logUp.set_password(password)
        logUp.username = email
        logUp.save()
        return redirect("/sfHome")
    return render(request, "sfProfile.html", {"data": data})


def sfChangeImage(request):
    id = request.session["id"]
    data = Startupfounder.objects.get(id=id)
    if request.method == "POST":
        img = request.FILES["file"]

        data.document = img
        data.save()
        return redirect("/sfHome")
    return render(request, "sfChangeImage.html", {"data": data})


def sfPost(request):
    id = request.session["id"]
    if request.method == "POST":
        idea = request.POST["idea"]
        description = request.POST["description"]
        user = Startupfounder.objects.get(id=id)
        db = Idea.objects.create(idea=idea, desc=description, user=user)
        db.save()

    return render(request, "sfPost.html")


def sfViewSelfPost(request):
    id = request.session["id"]

    data = Idea.objects.filter(user=id)
    return render(request, "sfViewSelfPost.html", {"data": data})


def sfUpdateIdea(request):
    id = request.GET["id"]
    data = Idea.objects.get(id=id)
    if request.method == "POST":
        idea = request.POST["idea"]
        description = request.POST["description"]
        data.idea = idea
        data.desc = description
        data.save()
        return redirect("/sfViewSelfPost")
    return render(request, "sfUpdateIdea.html", {"data": data})


def sfDeleteIdea(request):
    id = request.GET["id"]
    data = Idea.objects.get(id=id)
    data.delete()

    return redirect("/sfViewSelfPost")


def sfViewIdea(request):
    id = request.GET["post"]
    sfid = request.session["id"]

    data = Idea.objects.get(id=id)
    if request.method == "POST":
        comment = request.POST["comment"]

        user = Startupfounder.objects.get(id=sfid)
        db = Comments.objects.create(comment=comment, idea=data, user=user)
        db.save()

    comments = Comments.objects.filter(idea=id)
    return render(request, "sfViewIdea.html", {"data": data, "comments": comments})


def sfViewSf(request):
    id = request.GET["sfid"]
    user = Startupfounder.objects.get(id=id)

    post = Idea.objects.filter(user=id)
    return render(request, "sfViewSf.html", {"user": user, "post": post})


def sfViewInvestemntOffers(request):
    id = request.session["id"]
    data = Investmentinterest.objects.filter(idea__user__id=id)
    return render(request, "sfViewInvestemntOffers.html", {"data": data})


def sfViewPayments(request):
    id = request.session["id"]

    data = Payment.objects.filter(statup=id)
    return render(request, "sfViewPayments.html", {"data": data})


def sfOnInvestmentOffer(request):
    ininid = request.GET["ininid"]
    status = request.GET["status"]
    data = Investmentinterest.objects.get(id=ininid)
    data.status = status
    data.save()
    return redirect("/sfViewInvestemntOffers")


def sfAddFeedBack(request):
    id = request.session["id"]
    if request.method == "POST":
        feedback = request.POST["feedback"]
        user = Startupfounder.objects.get(id=id)

        db = Feedback.objects.create(feedback=feedback, user=user)
        db.save()
    data = Feedback.objects.filter(user=id)
    return render(request, "sfAddFeedBack.html", {"data": data})


def sfChat(request):
    sender = request.session["email"]
    # qry = f"SELECT DISTINCT sender, receiver FROM `chat` WHERE `sender`='{sender}' OR `receiver`='{sender}'"
    data = Chat.objects.filter(Q(sender=sender) | Q(receiver=sender)).distinct()
    return render(request, "sfChat.html", {"data": data, "user": sender})


def sfChatPer(request):
    sender = request.session["email"]
    receiver = request.GET["email"]
    updateStatus = Chat.objects.filter(Q(sender=receiver) & Q(receiver=sender)).update(
        status="Seen"
    )
    if request.method == "POST":
        msg = request.POST["msg"]
        db = Chat.objects.create(sender=sender, receiver=receiver, message=msg)
        db.save()
    messages = Chat.objects.filter(
        Q(sender=sender, receiver=receiver) | Q(sender=receiver, receiver=sender)
    )
    return render(request, "sfChatPer.html", {"messages": messages, "user": sender})


def workSpaces(request):
    data = WorkSpace.objects.exclude(status="Occupied")
    return render(request, "workSpaces.html", {"data": data})


def bookWorkSpace(request):
    id = request.GET["id"]
    amount = request.GET["amount"]
    uid = request.session["id"]
    sfid = Startupfounder.objects.get(id=uid)

    if request.POST:
        chStatus = WorkSpace.objects.filter(id=id).update(status="Occupied", sfid=sfid)
        messages.success(request, "Payment Success")
        return redirect("/viewBookings")
    return render(request, "paymentForm.html", {"amount": amount})


def viewBookings(request):
    uid = request.session["id"]
    data = WorkSpace.objects.filter(sfid=uid)
    return render(request, "viewBookings.html", {"data": data})
