

# Class: SelectValidationSchema 


_Extends schema to define a specific set of validation rules that can be used for select options._





<!--
URI: [https://specification.margo.org/data-model/SelectValidationSchema](https://specification.margo.org/data-model/SelectValidationSchema)
-->





```mermaid
 classDiagram
    class SelectValidationSchema
    click SelectValidationSchema href "../SelectValidationSchema/"
      Schema <|-- SelectValidationSchema
        click Schema href "../Schema/"
      
      SelectValidationSchema : allowEmpty
        
      SelectValidationSchema : dataType
        
      SelectValidationSchema : multiselect
        
      SelectValidationSchema : name
        
      SelectValidationSchema : options
        
      
```





## Inheritance
* [Schema](Schema.md)
    * **SelectValidationSchema**


## Attributes

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [allowEmpty](allowEmpty.md) | 0..1 <br/> [boolean](boolean.md) | If true, indicates a value must be provided | direct |
| [multiselect](multiselect.md) | 0..1 <br/> [boolean](boolean.md) | If true, indicates multiple values can be selected | direct |
| [options](options.md) | 1..* <br/> [string](string.md) | This provides the list of acceptable options the user can select from | direct |
| [name](name.md) | 1 <br/> [string](string.md) | The name of the schema rule | [Schema](Schema.md) |
| [dataType](dataType.md) | 1 <br/> [string](string.md) | Indicates the expected data type for the user provided value | [Schema](Schema.md) |















<!--
## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/SelectValidationSchema |
| native | https://specification.margo.org/data-model/SelectValidationSchema |


-->



??? note "Only relevant for contributors of the specification"

    ## LinkML Source

    <!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

    ### Direct

    ??? note "Details"
        ```yaml
        name: SelectValidationSchema
        description: Extends schema to define a specific set of validation rules that can
          be used for select options.
        from_schema: https://specification.margo.org/data-model
        is_a: Schema
        attributes:
          allowEmpty:
            name: allowEmpty
            description: If true, indicates a value must be provided. Default is false if
              not provided.
            from_schema: https://specification.margo.org/application-schema
            domain_of:
            - TextValidationSchema
            - BooleanValidationSchema
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            - SelectValidationSchema
            range: boolean
            required: false
          multiselect:
            name: multiselect
            description: If true, indicates multiple values can be selected. If multiple values
              can be selected the resulting value is an array of the selected values. The
              default is false if not provided.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            domain_of:
            - SelectValidationSchema
            range: boolean
            required: false
          options:
            name: options
            description: This provides the list of acceptable options the user can select
              from. The data type for each option must match the parameter setting’s data
              type.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            domain_of:
            - SelectValidationSchema
            range: string
            required: true
            multivalued: true

        ```

    ### Induced

    ??? note "Details"
        ```yaml
        name: SelectValidationSchema
        description: Extends schema to define a specific set of validation rules that can
          be used for select options.
        from_schema: https://specification.margo.org/data-model
        is_a: Schema
        attributes:
          allowEmpty:
            name: allowEmpty
            description: If true, indicates a value must be provided. Default is false if
              not provided.
            from_schema: https://specification.margo.org/application-schema
            alias: allowEmpty
            owner: SelectValidationSchema
            domain_of:
            - TextValidationSchema
            - BooleanValidationSchema
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            - SelectValidationSchema
            range: boolean
            required: false
          multiselect:
            name: multiselect
            description: If true, indicates multiple values can be selected. If multiple values
              can be selected the resulting value is an array of the selected values. The
              default is false if not provided.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            alias: multiselect
            owner: SelectValidationSchema
            domain_of:
            - SelectValidationSchema
            range: boolean
            required: false
          options:
            name: options
            description: This provides the list of acceptable options the user can select
              from. The data type for each option must match the parameter setting’s data
              type.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            alias: options
            owner: SelectValidationSchema
            domain_of:
            - SelectValidationSchema
            range: string
            required: true
            multivalued: true
          name:
            name: name
            description: The name of the schema rule. This used in the [setting](#setting-attributes)
              to link the setting to the schema rule.
            from_schema: https://specification.margo.org/application-schema
            identifier: true
            alias: name
            owner: SelectValidationSchema
            domain_of:
            - Component
            - Parameter
            - DeploymentMetadata
            - ApplicationMetadata
            - Author
            - Organization
            - Section
            - Setting
            - Schema
            - ComponentStatus
            range: string
            required: true
          dataType:
            name: dataType
            description: Indicates the expected data type for the user provided value. Accepted
              values are string, integer, double, boolean, array[string], array[integer],
              array[double], array[boolean]. At a minimum, the provided parameter value MUST
              match the schema's data type if no other validation rules are provided.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            alias: dataType
            owner: SelectValidationSchema
            domain_of:
            - Schema
            range: string
            required: true

        ```