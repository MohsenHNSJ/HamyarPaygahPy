# Notes about project

## Issues

### Mission details response from server

When requesting mission details from server, the response is funny,
It's like they made it in a rush and never bothered to update.
I'm no Bill gates, but i at least try to use some tools to help me
program better and cleaner. They just made a bit messy shit. :/

- The following values are not known and not processed:

```xml
<a:Asm>false</a:Asm>
<a:DarmaniTahvilBedoonRezayat>false</a:DarmaniTahvilBedoonRezayat>
<a:FotHozoor>false</a:FotHozoor>
<a:HospitalText>-</a:HospitalText>
<a:Sar>false</a:Sar>
<a:SucktonBad>false</a:SucktonBad>
<a:TromaSayer>false</a:TromaSayer>
```

- This value is unknown to me and has no value, therefore
it's not processed currently: ```<a:Ranande>-</a:Ranande>```

- This variable has mistyped name: ```<a:KMesidanBePaygah>```

- This variable is not fully pascal case named: ```<a:TahvilBedarmani>```

- This variable name is written in two languages! ```<a:BimarName>```

- This variable is for age but it also stores the word
"age" in it: ```<a:Age>```

- Instead of saving the gender in one variable,
it's saved on multiple boolean states:
```<a:IsMozakar>``` ```<a:IsMoanas>``` ```<a:IsNamoshakhas>```

- Mistyped variable name: ```<a:ShomareSerialParvade>```

- A simple yes or no question of wether the patient is an iranian
or not is saved in two boolean variables:
```<a:IsIrani>``` ```<a:IsGheirIrani>```

- ```<a:AfzayeshFesharKoon>``` Really? :/

- ```<a:Haipogelesimi>``` What english class you have been?!

- ```<a:Hipergelesimi>``` Hiper Market ...

- The server cannot save ```Low blood pressure``` as the type of illness.
This options is available in the client, but server ignores it
and does not save it.

- And many more that i don't want to care anymore...
