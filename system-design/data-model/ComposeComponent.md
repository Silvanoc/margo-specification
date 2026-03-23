

# Class: ComposeComponent 



<!--
URI: [https://specification.margo.org/data-model/ComposeComponent](https://specification.margo.org/data-model/ComposeComponent)
-->





```mermaid
 classDiagram
    class ComposeComponent
    click ComposeComponent href "../ComposeComponent/"
      Component <|-- ComposeComponent
        click Component href "../Component/"
      
      ComposeComponent : name
        
      ComposeComponent : properties
        
          
    
        
        
        ComposeComponent --> "1" ComponentProperties : properties
        click ComponentProperties href "../ComponentProperties/"
    

        
      
```





## Inheritance
* [Component](Component.md)
    * **ComposeComponent**


## Attributes

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [string](string.md) | A unique name used to identify the component package | [Component](Component.md) |
| [properties](properties.md) | 1 <br/> [ComponentProperties](ComponentProperties.md) | A dictionary element specifying the component packages's deployment details | [Component](Component.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ComposeDeploymentProfile](ComposeDeploymentProfile.md) | [components](components.md) | range | [ComposeComponent](ComposeComponent.md) |
| [ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) | [components](components.md) | range | [ComposeComponent](ComposeComponent.md) |












<!--
## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/ComposeComponent |
| native | https://specification.margo.org/data-model/ComposeComponent |


-->



??? note "Only relevant for contributors of the specification"

    ## LinkML Source

    <!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

    ### Direct

    ??? note "Details"
        ```yaml
        name: ComposeComponent
        from_schema: https://specification.margo.org/data-model
        is_a: Component

        ```

    ### Induced

    ??? note "Details"
        ```yaml
        name: ComposeComponent
        from_schema: https://specification.margo.org/data-model
        is_a: Component
        attributes:
          name:
            name: name
            description: A unique name used to identify the component package. For helm installations
              the name will be used as the chart name. The name must be lower case letters
              and numbers and MAY contain dashes.  Uppercase letters, underscores and periods
              MUST NOT be used.
            from_schema: https://specification.margo.org/deployments
            rank: 1000
            alias: name
            owner: ComposeComponent
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
          properties:
            name: properties
            description: A dictionary element specifying the component packages's deployment
              details.  See the [Component Properties](#componentproperties-attributes) section
              below.
            from_schema: https://specification.margo.org/deployments
            rank: 1000
            alias: properties
            owner: ComposeComponent
            domain_of:
            - Component
            - DeviceCapabilitiesManifest
            range: ComponentProperties
            required: true

        ```