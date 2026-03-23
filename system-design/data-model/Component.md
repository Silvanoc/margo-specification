

# Class: Component 


_A class representing a component of a deployment profile._





<!--
URI: [https://specification.margo.org/data-model/Component](https://specification.margo.org/data-model/Component)
-->





```mermaid
 classDiagram
    class Component
    click Component href "../Component/"
      Component <|-- HelmComponent
        click HelmComponent href "../HelmComponent/"
      Component <|-- ComposeComponent
        click ComposeComponent href "../ComposeComponent/"
      
      Component : name
        
      Component : properties
        
          
    
        
        
        Component --> "1" ComponentProperties : properties
        click ComponentProperties href "../ComponentProperties/"
    

        
      
```





## Inheritance
* **Component**
    * [HelmComponent](HelmComponent.md)
    * [ComposeComponent](ComposeComponent.md)


## Attributes

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [string](string.md) | A unique name used to identify the component package | direct |
| [properties](properties.md) | 1 <br/> [ComponentProperties](ComponentProperties.md) | A dictionary element specifying the component packages's deployment details | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DeploymentProfile](DeploymentProfile.md) | [components](components.md) | range | [Component](Component.md) |
| [DeploymentProfileDescription](DeploymentProfileDescription.md) | [components](components.md) | range | [Component](Component.md) |












<!--
## Identifier and Mapping Information





### Schema Source


* from schema: https://specification.margo.org/data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | https://specification.margo.org/data-model/Component |
| native | https://specification.margo.org/data-model/Component |


-->



??? note "Only relevant for contributors of the specification"

    ## LinkML Source

    <!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

    ### Direct

    ??? note "Details"
        ```yaml
        name: Component
        description: A class representing a component of a deployment profile.
        from_schema: https://specification.margo.org/data-model
        attributes:
          name:
            name: name
            description: A unique name used to identify the component package. For helm installations
              the name will be used as the chart name. The name must be lower case letters
              and numbers and MAY contain dashes.  Uppercase letters, underscores and periods
              MUST NOT be used.
            from_schema: https://specification.margo.org/deployments
            rank: 1000
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
            domain_of:
            - Component
            - DeviceCapabilitiesManifest
            range: ComponentProperties
            required: true

        ```

    ### Induced

    ??? note "Details"
        ```yaml
        name: Component
        description: A class representing a component of a deployment profile.
        from_schema: https://specification.margo.org/data-model
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
            owner: Component
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
            owner: Component
            domain_of:
            - Component
            - DeviceCapabilitiesManifest
            range: ComponentProperties
            required: true

        ```