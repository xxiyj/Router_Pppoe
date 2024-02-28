function orgAuthPwd(a) {
    return securityEncode("RDpbLfCPsJZ7fiv", a, "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU43odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9aYb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoouyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ1xtXcPcf1aT303wAQhv66qzW")
}

function securityEncode(a, b, c) {
    var e = "", f, g, h, k, l = 187, n = 187;
    g = a.length;
    h = b.length;
    k = c.length;
    f = g > h ? g : h;
    for (var p = 0; p < f; p++)
        n = l = 187,
        p >= g ? n = b.charCodeAt(p) : p >= h ? l = a.charCodeAt(p) : (l = a.charCodeAt(p),
        n = b.charCodeAt(p)),
        e += c.charAt((l ^ n) % k);
    return e
}