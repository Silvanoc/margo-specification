# Margo Data Model

Margo specification involves complex, interrelated data structures that are used for multiple, different purposes.
This data model documents the mentioned data structures and their relationships.

<!--
URI: https://specification.margo.org/data-model

Name: DataModel
-->



## Interfacing Classes

These are the classes directly participating in Margo interfaces (e.g. APIs):

| Class | Description |
| --- | --- |
| [ApplicationDescription](ApplicationDescription.md) | Root class for an application description |
| [ApplicationDeployment](ApplicationDeployment.md) | A class representing the desired state of an entity |
| [DeviceCapabilitiesManifest](DeviceCapabilitiesManifest.md) | Capabilities of a device on which applications can be deployed |
| [DesiredStateManifest](DesiredStateManifest.md) | Manifest from the Workload Fleet Manager, representing the complete desired w... |
| [DeploymentStatusManifest](DeploymentStatusManifest.md) |  |


??? note "Very long table with all the classes in the Margo data model"

    ## All Classes

    These are all the classes involved in the Margo data model:

    | Class | Description |
    | --- | --- |
    | [ApplicationDeployment](ApplicationDeployment.md) | A class representing the desired state of an entity |
    | [ApplicationDescription](ApplicationDescription.md) | Root class for an application description |
    | [ApplicationMetadata](ApplicationMetadata.md) | Metadata about the application |
    | [Author](Author.md) | Information about the application's author |
    | [Bundle](Bundle.md) | Describes an archive containing all referenced ApplicationDeployment YAMLs |
    | [Catalog](Catalog.md) | Catalog metadata for displaying the application |
    | [CatalogApplicationMetadata](CatalogApplicationMetadata.md) | Metadata specific to the application |
    | [CommunicationInterface](CommunicationInterface.md) | Communication interface of a device |
    | [Component](Component.md) | A class representing a component of a deployment profile |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComposeComponent](ComposeComponent.md) |  |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HelmComponent](HelmComponent.md) |  |
    | [ComponentProperties](ComponentProperties.md) | Properties dictionary for component deployment details |
    | [Configuration](Configuration.md) | Configuration layout and validation rules |
    | [CPU](CPU.md) | CPU element specifying the CPU requirements for the application |
    | [Deployment](Deployment.md) | List of deployment objects describing each workload |
    | [DeploymentAnnotations](DeploymentAnnotations.md) | A class representing annotations |
    | [DeploymentMetadata](DeploymentMetadata.md) | Metadata associated with the desired state |
    | [DeploymentProfile](DeploymentProfile.md) | Represents a deployment configuration for the application |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComposeDeploymentProfile](ComposeDeploymentProfile.md) |  |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DeploymentProfileDescription](DeploymentProfileDescription.md) | Represents a deployment configuration for the application |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComposeDeploymentProfileDescription](ComposeDeploymentProfileDescription.md) |  |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HelmDeploymentProfileDescription](HelmDeploymentProfileDescription.md) |  |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HelmDeploymentProfile](HelmDeploymentProfile.md) |  |
    | [DeploymentStatusManifest](DeploymentStatusManifest.md) |  |
    | [DesiredStateManifest](DesiredStateManifest.md) | Manifest from the Workload Fleet Manager, representing the complete desired w... |
    | [DeviceCapabilitiesManifest](DeviceCapabilitiesManifest.md) | Capabilities of a device on which applications can be deployed |
    | [Error](Error.md) |  |
    | [Organization](Organization.md) | Information about the providing organization |
    | [Parameter](Parameter.md) | Defines a configurable parameter for the application |
    | [Peripheral](Peripheral.md) | Peripheral hardware of a device |
    | [Properties](Properties.md) |  |
    | [Resources](Resources.md) | Required resources element specifying the resources required to install the a... |
    | [Schema](Schema.md) | Defines data type and rules for validating user provided parameter values |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BooleanValidationSchema](BooleanValidationSchema.md) | Extends schema to define a boolean-specific set of validation rules that can ... |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NumericDoubleValidationSchema](NumericDoubleValidationSchema.md) | Extends schema to define a double-specific set of validation rules that can b... |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NumericIntegerValidationSchema](NumericIntegerValidationSchema.md) | Extends schema to define a integer-specific set of validation rules that can ... |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SelectValidationSchema](SelectValidationSchema.md) | Extends schema to define a specific set of validation rules that can be used ... |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextValidationSchema](TextValidationSchema.md) | Extends schema to define a string/text-specific set of validation rules that ... |
    | [Section](Section.md) | Named sections within the configuration layout |
    | [Setting](Setting.md) | Individual configuration settings |
    | [Spec](Spec.md) | Specification details of the desired state |
    | [Status](Status.md) |  |
    | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComponentStatus](ComponentStatus.md) | Status of a component deployment |
    | [Target](Target.md) | Specifies where the parameter applies in the deployment |
    
    

<!-- 
## Slots

| Slot | Description |
| --- | --- |
| [allowEmpty](allowEmpty.md) | If true, indicates a value must be provided |
| [annotations](annotations.md) | Defines the application ID and unique identifier associated to the deployment... |
| [apiVersion](apiVersion.md) | Identifier of the version of the API the object definition follows |
| [application](application.md) | Application element specifying the application specific metadata |
| [applicationId](applicationId.md) | An identifier for the application |
| [architectures](architectures.md) | The CPU architectures supported by the application |
| [author](author.md) | Author element specifying metadata about the application's author |
| [bundle](bundle.md) | Package optimization containing multiple ApplicationDeployment YAMLs |
| [catalog](catalog.md) | Catalog element specifying the application's metadata for enabling its discov... |
| [code](code.md) |  |
| [components](components.md) | Component element indicating the components to deploy when installing the app... |
| [configuration](configuration.md) | Configuration element specifying how parameters should be displayed to the us... |
| [cores](cores.md) | The required amount of CPU cores the application must use to run in its full ... |
| [cpu](cpu.md) | CPU element specifying the CPU requirements for the application |
| [dataType](dataType.md) | Indicates the expected data type for the user provided value |
| [deploymentId](deploymentId.md) | The UUID of the deployment |
| [deploymentProfile](deploymentProfile.md) | Section that defines deployment details including type and components |
| [deploymentProfiles](deploymentProfiles.md) | Deployment profiles element specifying the types of deployments the applicati... |
| [deployments](deployments.md) | List of deployment objects describing each workload |
| [description](description.md) |  |
| [descriptionFile](descriptionFile.md) | Link to the file containing the application's full description |
| [digest](digest.md) | Digest of the bundle archive |
| [email](email.md) | Email address of the application's creator |
| [error](error.md) |  |
| [icon](icon.md) | Link to the icon file (e |
| [id](id.md) | The unique identifier UUID of the deployment specification |
| [immutable](immutable.md) | If true, indicates the parameter value MUST not be changed once it has been s... |
| [interfaces](interfaces.md) | Interfaces element specifying the communication interfaces required to run th... |
| [keyLocation](keyLocation.md) | URL for the public key used to validate a digitally signed package |
| [kind](kind.md) | Must be `ApplicationDeployment` |
| [licenseFile](licenseFile.md) | Link to the file that details the application's license |
| [manifestVersion](manifestVersion.md) |  |
| [manufacturer](manufacturer.md) | The name of the manufacturer |
| [maxLength](maxLength.md) | If set, indicates the maximum number of characters the value must have to be ... |
| [maxPrecision](maxPrecision.md) | If set, indicates the maximum level of precision the value must have to be co... |
| [maxValue](maxValue.md) | If set, indicates the maximum allowed integer value the value must have to be... |
| [mediaType](mediaType.md) | MUST be application/vnd |
| [memory](memory.md) | The minimum amount of memory required |
| [message](message.md) |  |
| [metadata](metadata.md) | Metadata element specifying characteristics about the application deployment |
| [minLength](minLength.md) | If set, indicates the minimum number of characters the value must have to be ... |
| [minPrecision](minPrecision.md) | If set, indicates the minimum level of precision the value must have to be co... |
| [minValue](minValue.md) | If set, indicates the minimum allowed integer value the value must have to be... |
| [model](model.md) | The model of the peripheral |
| [modelNumber](modelNumber.md) | Defines the model number of the device |
| [multiselect](multiselect.md) | If true, indicates multiple values can be selected |
| [name](name.md) | A unique name used to identify the component package |
| [namespace](namespace.md) | When deploying to Kubernetes, the namespace the manifest is added under |
| [options](options.md) | This provides the list of acceptable options the user can select from |
| [organization](organization.md) | Organization element specifying metadata about the organization/company provi... |
| [packageLocation](packageLocation.md) | URL indicating the Compose package's location |
| [parameter](parameter.md) | The name of the [parameter](#parameter-attributes) the setting is associated ... |
| [parameters](parameters.md) | Describes the configured parameters applied via the end-user |
| [peripherals](peripherals.md) | Peripherals element specifying the peripherals required to run the applicatio... |
| [pointer](pointer.md) | The name of the parameter in the deployment configuration |
| [properties](properties.md) | A dictionary element specifying the component packages's deployment details |
| [regexMatch](regexMatch.md) | If set, indicates a regular expression to use to validate the value |
| [releaseNotes](releaseNotes.md) | Statement about the changes for this application's release |
| [repository](repository.md) | Repository location for the component |
| [requiredResources](requiredResources.md) | Required resources element specifying the resources required to install the a... |
| [resources](resources.md) | Element that defines the device's resources available to the application depl... |
| [revision](revision.md) | Revision version for the component |
| [roles](roles.md) | Element that defines the device role it can provide to the Margo environment |
| [schema](schema.md) | Schema is used to provide details about how to validate each parameter value |
| [sections](sections.md) | Sections are used to group related parameters together, so it is possible to ... |
| [serialNumber](serialNumber.md) | Defines the serial number of the device |
| [settings](settings.md) | Settings are used to provide instructions to the workload orchestration softw... |
| [site](site.md) | Link to the application's website |
| [sizeBytes](sizeBytes.md) | Optional unsigned 64-bit advisory estimate of the decoded payload length in b... |
| [spec](spec.md) | Spec element that defines deployment profile and parameters associated with t... |
| [state](state.md) |  |
| [status](status.md) |  |
| [storage](storage.md) | The amount of storage required for the application to run |
| [tagline](tagline.md) | The application's slogan |
| [tags](tags.md) | An array of strings that can be used to provide additional context for the ap... |
| [targets](targets.md) | Used to indicate which component the value should be applied to when installi... |
| [timeout](timeout.md) | Time to wait for component installation to complete, formatted as "##m##s" |
| [type](type.md) | Defines the type of this deployment configuration for the application |
| [url](url.md) | Content-addressable retrieval endpoint for the bundle of the form /api/v1/cli... |
| [value](value.md) | The parameter's default value |
| [vendor](vendor.md) | Defines the device vendor |
| [version](version.md) | The application's version |
| [wait](wait.md) | If True, indicates the device waits for the component installation to complet... |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CommunicationInterfaceType](CommunicationInterfaceType.md) |  |
| [CpuArchitectureType](CpuArchitectureType.md) |  |
| [DeviceRole](DeviceRole.md) |  |
| [PeripheralType](PeripheralType.md) |  |
| [State](State.md) |  |


## Types

| Type | Description |
| --- | --- |
| [boolean](boolean.md) | A binary (true or false) value |
| [curie](curie.md) | a compact URI |
| [date](date.md) | a date (year, month and day) in an idealized calendar |
| [date_or_datetime](date_or_datetime.md) | Either a date or a datetime |
| [datetime](datetime.md) | The combination of a date and time |
| [decimal](decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [DigestType](DigestType.md) | Hash that identifies an element by its content |
| [double](double.md) | A real number that conforms to the xsd:double specification |
| [float](float.md) | A real number that conforms to the xsd:float specification |
| [integer](integer.md) | An integer |
| [jsonpath](jsonpath.md) | A string encoding a JSON Path |
| [jsonpointer](jsonpointer.md) | A string encoding a JSON Pointer |
| [ncname](ncname.md) | Prefix part of CURIE |
| [nodeidentifier](nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [objectidentifier](objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [SizeBytesType](SizeBytesType.md) | Size of an element in bytes |
| [sparqlpath](sparqlpath.md) | A string encoding a SPARQL Property Path |
| [string](string.md) | A character string |
| [time](time.md) | A time object represents a (local) time of day, independent of any particular... |
| [uri](uri.md) | a complete URI |
| [uriorcurie](uriorcurie.md) | a URI or a CURIE |
| [UrlType](UrlType.md) | Endpoint (URL without schema and domain) associated to an element |


## Subsets

| Subset | Description |
| --- | --- |
| [api_resources](api_resources.md) |  |

-->