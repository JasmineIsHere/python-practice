import java.util.Iterator;
import java.util.Set;
import com.google.gson.*;

public class jsonTraversal {
    public JsonObject findJsonObject (JsonObject data, String targetKey){
        if (! data.has(targetKey)){
            //key not found; go down another level
            Set keys = data.keySet();
            Iterator it = keys.iterator();
            while (it.hasNext()){
                //check each key
                JsonElement innerElement = data.get((String)it.next());
                if (innerElement.isJsonObject()){
                    JsonObject innerObject = innerElement.getAsJsonObject();
                    return findJsonObject(innerObject, targetKey);
                }
            }
//            JsonObject innerLayer = data.getAsString();
        } else if (data.has(targetKey)) {
            return data;
        }
        return null;
    }
}
