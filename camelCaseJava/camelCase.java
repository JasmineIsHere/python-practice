class camelCase{
    //from "helloWorld" to "Hello World"
     public String breakCamelCase(String string){
         String formattedString = "";
         String regex = "([a-z])([A-Z]+)";
         String replacement = "$1 $2";
         formattedString = string.replaceAll(regex, replacement);
         formattedString = formattedString.substring(0, 1).toUpperCase() + formattedString.substring(1);
         return formattedString;
     }

     //from "Hello World" to "helloWorld"
     public String toCamelCase(String string){
         string = string.substring(0, 1).toLowerCase() + string.substring(1);

         string = string.replaceAll("\\s", "");
         return string;
     }

}