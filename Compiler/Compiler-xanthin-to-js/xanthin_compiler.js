
  function comp(fname){
    g = fname.replace("message.show","console.log");
    d = g.replace("void main or mains(","");
    k = d.replace("@","class");
    s = k.replace("=>","{");
    find = s.replace("<=","}");
    ac = find.replace("action","function");
    debug = ac.replace("?","(");
    x = debug.replace("!",")");
    n = x.replace("use","import");
    done = n.replace("add *","");
    mf = done.replace("::","==");
    mone = mf.replace(":","=");
    mision = mone.replace("reback","return");
    nara = mision.replace(" DOT ",".");
    back = nara.replace(" AND ","_");
    canh = back.replace("put in place of","replace");
    me = canh.replace("++","__");
    js = me.replace("Get Element By ID","getElementById");
    eval(js);
  }
