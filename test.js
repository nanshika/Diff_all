var this_year = new Date().getFullYear();
var t = "a	b c";
document.write(t + '<BR>');
var t2 = t.replace('\t', '');
document.write(t2 + '<BR>');
document.write(t + '<BR>');
document.write('<BR><BR><BR>');

document.write(new Date().getDate() + '\n');
for (var date = 1; date < 32; date++) {
    var tar_year = this_year + 1 - date;
    if (tar_year > 2005) {
        document.write(tar_year + '<BR>');
    }
}
