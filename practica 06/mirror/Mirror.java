package tudelft.mirror;

public class Mirror {

    public String mirrorEnds(String string) {
        String mirror = "";

        int begin = 0;
        int end = string.length() - 1;

        for (; begin < string.length(); begin++) {
            if (string.charAt(begin) == string.charAt(end - begin)) {
               // se usa charAt(begin) en lugar de charAt(end)
                mirror += string.charAt(begin);
            }
            else {
                break;
            }
        }
        //se elimina la condición incorrecta y se devuelve directamente mirror
        return mirror;
    }
}
