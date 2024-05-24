// CREATED AT 12/20/2018
// PROJECT NUMBER = 3
// LANGAUGE USED "SWIFT"
// This function prints out the most used application

var var1 = 0
var var2 = 0
var vp = 0
var app = ""

func Problem_Solving(FB: Int,TW: Int,IS: Int,SC: Int) {
    if IS > SC {
        var1 = IS
    }else if SC > IS {
        var1 = SC
    }
    if FB > TW {
        var2 = FB
    }else if TW > FB {
        var2 = TW
    }
    if var1 > var2 {
        vp = var1
    }else if var2 > var1 {
        vp = var2
    }
    if vp == FB {
        app = "FaceBook"
    }else if vp == TW {
        app = "Twitter"
    }else if vp == IS {
        app = "Instagram"
    }else if vp == SC {
        app = "Snapchat"
    }
    print("Your most used app is \(app)")
}

Problem_Solving(FB: 3,TW: 7,IS: 4,SC: 5)