

# Class: NumericDoubleValidationSchema 


_Extends schema to define a double-specific set of validation rules that can be used._





<!--
URI: [https://specification.margo.org/data-model/NumericDoubleValidationSchema](https://specification.margo.org/data-model/NumericDoubleValidationSchema)
-->





```mermaid
 classDiagram
    class NumericDoubleValidationSchema
    click NumericDoubleValidationSchema href "../NumericDoubleValidationSchema/"
      Schema <|-- NumericDoubleValidationSchema
        click Schema href "../Schema/"
      
      NumericDoubleValidationSchema : allowEmpty
        
      NumericDoubleValidationSchema : dataType
        
      NumericDoubleValidationSchema : maxPrecision
        
      NumericDoubleValidationSchema : maxValue
        
      NumericDoubleValidationSchema : minPrecision
        
      NumericDoubleValidationSchema : minValue
        
      NumericDoubleValidationSchema : name
        
      
```





## Inheritance
* [Schema](Schema.md)
    * **NumericDoubleValidationSchema**


## Attributes

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [allowEmpty](allowEmpty.md) | 0..1 <br/> [boolean](boolean.md) | If true, indicates a value must be provided | direct |
| [minValue](minValue.md) | 0..1 <br/> [float](float.md) | If set, indicates the minimum value to be considered valid | direct |
| [maxValue](maxValue.md) | 0..1 <br/> [float](float.md) | If set, indicates the maximum value to be considered valid | direct |
| [minPrecision](minPrecision.md) | 0..1 <br/> [integer](integer.md) | If set, indicates the minimum level of precision the value must have to be co... | direct |
| [maxPrecision](maxPrecision.md) | 0..1 <br/> [integer](integer.md) | If set, indicates the maximum level of precision the value must have to be co... | direct |
| [name](name.md) | 1 <br/> [string](string.md) | The name of the schema rule | [Schema](Schema.md) |
| [dataType](dataType.md) | 1 <br/> [string](string.md) | Indicates the expected data type for the user provided value | [Schema](Schema.md) |















<!--
## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/NumericDoubleValidationSchema |
| native | https://specification.margo.org/data-model/NumericDoubleValidationSchema |


-->



??? note "Only relevant for contributors of the specification"

    ## LinkML Source

    <!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

    ### Direct

    ??? note "Details"
        ```yaml
        name: NumericDoubleValidationSchema
        description: Extends schema to define a double-specific set of validation rules that
          can be used.
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
          minValue:
            name: minValue
            description: If set, indicates the minimum value to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            domain_of:
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            range: float
            required: false
          maxValue:
            name: maxValue
            description: If set, indicates the maximum value to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            domain_of:
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            range: float
            required: false
          minPrecision:
            name: minPrecision
            description: If set, indicates the minimum level of precision the value must have
              to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            domain_of:
            - NumericDoubleValidationSchema
            range: integer
            required: false
          maxPrecision:
            name: maxPrecision
            description: If set, indicates the maximum level of precision the value must have
              to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            domain_of:
            - NumericDoubleValidationSchema
            range: integer
            required: false

        ```

    ### Induced

    ??? note "Details"
        ```yaml
        name: NumericDoubleValidationSchema
        description: Extends schema to define a double-specific set of validation rules that
          can be used.
        from_schema: https://specification.margo.org/data-model
        is_a: Schema
        attributes:
          allowEmpty:
            name: allowEmpty
            description: If true, indicates a value must be provided. Default is false if
              not provided.
            from_schema: https://specification.margo.org/application-schema
            alias: allowEmpty
            owner: NumericDoubleValidationSchema
            domain_of:
            - TextValidationSchema
            - BooleanValidationSchema
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            - SelectValidationSchema
            range: boolean
            required: false
          minValue:
            name: minValue
            description: If set, indicates the minimum value to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            alias: minValue
            owner: NumericDoubleValidationSchema
            domain_of:
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            range: float
            required: false
          maxValue:
            name: maxValue
            description: If set, indicates the maximum value to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            alias: maxValue
            owner: NumericDoubleValidationSchema
            domain_of:
            - NumericIntegerValidationSchema
            - NumericDoubleValidationSchema
            range: float
            required: false
          minPrecision:
            name: minPrecision
            description: If set, indicates the minimum level of precision the value must have
              to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            alias: minPrecision
            owner: NumericDoubleValidationSchema
            domain_of:
            - NumericDoubleValidationSchema
            range: integer
            required: false
          maxPrecision:
            name: maxPrecision
            description: If set, indicates the maximum level of precision the value must have
              to be considered valid.
            from_schema: https://specification.margo.org/application-schema
            rank: 1000
            alias: maxPrecision
            owner: NumericDoubleValidationSchema
            domain_of:
            - NumericDoubleValidationSchema
            range: integer
            required: false
          name:
            name: name
            description: The name of the schema rule. This used in the [setting](#setting-attributes)
              to link the setting to the schema rule.
            from_schema: https://specification.margo.org/application-schema
            identifier: true
            alias: name
            owner: NumericDoubleValidationSchema
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
            owner: NumericDoubleValidationSchema
            domain_of:
            - Schema
            range: string
            required: true

        ```