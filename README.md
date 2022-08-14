# kadupul-flower
API for Person and Location Services

## General
### Diagrams


## FHIR
### Schemas
[Person:](http://hl7.org/fhir/person.html#resource)  General Information about a person independent of a specific health-related context.  [Visit FHIR site for more info on Usage](http://hl7.org/fhir/person.html#scope).

[Identifier:](http://hl7.org/fhir/datatypes.html#Identifier) The field represent the `Id` on the person object.  The field is a collection of numeric or alphanumeric strings.  The collection can included the GCP Healthcare ID &/or the Legacy ID.

[Link:](http://hl7.org/fhir/person-definitions.html#Person.link) The field contains a collection of references.  The reference schema is a [Link Target](http://hl7.org/fhir/references.html#Reference).  The Link Target will contain referational information for a Lead, Patient, and/or Marketing Profile.  The Target will not contain the full dataset for the Lead, Patient, and Merketing Profile.  Visit the [FHIR Reference](http://hl7.org/fhir/references.html#Reference) schema for full explanation of the dataset.