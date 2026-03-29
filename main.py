from flet import *
def main(page:Page):
    page.title = "Food"
    page.window.width= 390
    page.window.height = 740
    page.bgcolor = colors.WHITE
    page.window.top=10
    page.window.left=960

    def route(route):
        page.views.clear()
        page.views.append(
                View("/",
                     [
                    AppBar(title=Text("Food"),
                            color="white",
                            bgcolor="blue"),

                    Row([
                        Text("Foods",weight=FontWeight.BOLD,size=20),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Text("Last Week",weight=FontWeight.BOLD,size=20),
                        Text("\t\t\t"),
                        Text("This Week",weight=FontWeight.BOLD,size=20)
                    ]),

                    Row([
                        Text("ملوخية",weight=FontWeight.BOLD),
                        Text("" 
                        ""),
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),
                        
                    Row([
                        Text("كبسة  ",weight=FontWeight.BOLD),
                        Text("" 
                        ""),
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("لبن امو",weight=FontWeight.BOLD),
                        Text("" \
                        ""),
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("رز عخضرة",weight=FontWeight.BOLD),
                        Text("" \
                        ""),
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("بطاطة عدجاج",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                       
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("مجدرة",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("مجدرة حمرة",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                       
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("بطاطة مسلوقة وبيض",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                       
                        Text("\n"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("معكرونة",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                     
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("معكرونة بالبشميل",weight=FontWeight.BOLD), 
                        Text("" \
                        ""),                    
                        Text("\n"),
                        Text("\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("كبة",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                      
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("برغر",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("كرسبي",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("اسكلوب",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("زنغر",weight=FontWeight.BOLD),
                        Text("" \
                        ""),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),

                    Row([
                        Text("بروستد",weight=FontWeight.BOLD),                        
                        Text("\n"),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),
                        Text("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"),
                        Checkbox(),]),


                     ],
                     scroll=ScrollMode.ALWAYS)
            )

        page.update()
    def page_go(view):
        page.views.pop()
        back_page = page.views[-1]
        page.go(back_page.route)
    
    page.on_route_change = route
    page.on_view_pop = page_go
    page.go(page.route)
app(main)
