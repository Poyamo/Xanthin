fn mojoRUN(fname: &str) {
  let file = xan2read(fname ,"r")
  let low = file.read()
  let naa = fuc.replace("( ","(");
  let mkm = naa.replace("print ","print");
  let helpa = mkm.replace(" )",")");
  exec(fuc)
}
fn main(){
  println!("hi");
}
mojoRUN("xanthinMojoCore.🔥")
