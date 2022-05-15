# shopify-challenge
Shopify coding challenge

I have implemented the delete-undelete feature as an extension.
Just for my sanity, I have the CRUD operations separate from the extended feature. The feature allows marking an item as inactive, active, down for maintenance,
or promoted (to push an item to the top of the fetch results).

When an item is created, it is, by default, set as inactive - something I figured out the hard way from my work as a Software Engineer. So, after creating
an item, it needs to be "undeleted" or promoted, and only then would it be available for viewing. The API to change the status of an item also allows a comment
to be sent with it, that I have kept optional and avoided implementing cheks for, for simplicity's sake.

When items are viewed, the promoted ones are shown on the top (with no regard to the order in which they were updated), then the active ones, and at last the 
ones under maintenance (just so that I could add comments, and see how Product Managers would want to see them, had these been viewed on their dashboard).

I haven't implemented a database, and everything is IN MEMORY. The former would have been much, much, much more elegant. But, it is what it is, and I hope
a joke makes up for the bad experience - 


Boss told me that as a security guard, it's my job to watch the whole office.


I'm on season 4 but I'm not really sure what it's got to do with security. I guess I'll see them next week.
