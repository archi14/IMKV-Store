<h1>In Memory Key value Store</h1>

<h4> An in memory key value store similar to Redis. The data stored is transient and is in memory. Currently the store supports
  below functionalities.
  <ul>
    <li> Adding key and value [value is an object] </l1>
 <li>  Getting a key </l1>
 <li>  Searching for an attribute key and value and returning the corresponding keys </l1>
 <li>  Deleting existing key </l1>
 <li> Changing the value within an exisiting key </l1>
  </ul>
  
  <h4> The key is of type string, the value is a object again in format {key:value}, where key is again string but value can take
  any type from bool, int, float to string </h4>
  
  <h4> If during update of an attribute within a key, the type of the value differs, an error is thrown</h4>
  
  <h4> Sample Input</h4>
  <pre> 
        put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled false estimated_time 30
        get sde_bootcamp
        keys
        put sde_kickstart title SDE-Kickstart price 4000 enrolled true estimated_time 8
        get sde_kickstart
        keys
        put sde_kickstart title SDE-Kickstart price 4000.00 enrolled true estimated_time 8
        get sde_kickstart
        keys
        delete sde_bootcamp
        get sde_bootcamp
        keys
        put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled true estimated_time 30
        search price 30000.00
        search enrolled true
        exit
  </pre>
  
  <h4> Output after running the script with the above input </h4>
  <pre>
    title:SDE-Bootcamp, price:30000.0, enrolled:False, estimated_time:30
    sde_bootcamp
    title:SDE-Kickstart, price:4000, enrolled:True, estimated_time:8
    sde_bootcamp,sde_kickstart
    Data type Error
    title:SDE-Kickstart, price:4000, enrolled:True, estimated_time:8
    sde_bootcamp,sde_kickstart
    No entry found for sde_bootcamp
    sde_kickstart
    sde_bootcamp
    sde_kickstart,sde_bootcamp
    </pre>
  

