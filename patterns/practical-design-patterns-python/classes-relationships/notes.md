
![Uploading Screenshot 2024-11-07 at 22.32.48.png…]()

# Types of interactions within classes
1. Inheritance
2. Assosiation
3. Aggregation
4. Composition

## Inheritance
- Class inherits data and functionalities of another class (successor has all the fields and methods of anchestor) and commonly some additional functionality is added. 
- Follow principle `B is A`
- In fact is handy mechansim of DRY concept
```text
Example: Car -> Coupe
```

## Assosiation
- Classes assosiation is a relationship between classes, which allows one class (object) to call another class (object) and compose some logic from its name.
- `assosiation` means `dependency`
- Follows principle `B uses A` or `B interacts with A`
```text
Example: student goes to the universtity (uses uni to get knowledge).
```
Assosiation has 2 more subtypes: `aggregation` and `composition`
### Aggregation
Method of creating a new class (container) B from A.
- objects are equal
- objects might exist independently
- follow principle `B has A`
- if container will be deleted - another container might still leave

### Composition
Method of creating a new class (container) B from A.
- objects are not equal
- objects might not exist independently
- follow principle `B owns A`
- if container will be deleted - another container will be deleted as well


## Examle of Aggregation and Composition
Text editor owns `buffer` (composition). And uses file (aggregation). When closing text editor, buffer is deleted, however file remains.
