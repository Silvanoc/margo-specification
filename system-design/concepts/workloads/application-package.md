# Application Package

The Application Package, which is used to [distribute an application](../../overview/workloads.md) that shall be deployed as [workloads](../../personas-and-definitions/technical-lexicon.md#workload) on edge devices, comprises the following elements:
 
- The **Application Description**: a YAML document with the element `kind` defined as `ApplicationDescription`, which is stored in a file (for example named `margo.yaml`) and contains information about the application's [metadata](../../specification/application-package/application-description.md#metadata-attributes) (e.g., description, icon, release notes, license file, etc.), the application [components](../../personas-and-definitions/technical-lexicon.md#component) (e.g,  Helm charts, Compose Archive) which are defined in [deployment configurations](../../specification/application-package/application-description.md#deploymentprofile-attributes), and [configurable application parameters](../../specification/application-package/application-description.md#defining-configurable-application-parameters).  There SHALL be only one YAML file in the package root of kind `ApplicationDescription`.
- The **resources**, which are additional files associated with the application (e.g., manual, icon, release notes, license file, etc.) that may be used to display more information about the application in a UI such as an [application catalog](../../personas-and-definitions/technical-lexicon.md#application-catalog) or [marketplace](../../personas-and-definitions/technical-lexicon.md#workload-marketplace) or other informative outputs.

The Application Package SHALL follow a folder/file structure as such:

```yaml
/                                  # REQUIRED top-level directory 
└── <application description>.yaml # REQUIRED a YAML document with element 'kind' as 'ApplicationDescription' stored in a file  (e.g., 'margo.yaml')
└── resources                      # OPTIONAL folder with application files (e.g., icon, license file, release notes) that may be used for displaying additional information about the application
```

The Application Package SHALL be made available in an [Application Registry](./application-registry.md).

An application aggregates one or more [components](../personas-and-definitions/software-composition.md), which each link to one or more [OCI Containers](https://github.com/opencontainers). The components  referenced in the [Application Description](../../specification/application-package/application-description.md) are stored in a [Component Registry](../../personas-and-definitions/technical-lexicon.md#component-registry), and the linked containers are provided via a [Container Registry](../../personas-and-definitions/technical-lexicon.md#container-registry). Registries can be remote (i.e., Internet-accessible) or [local](../../concepts/workloads/local-registries.md) (i.e., accessible within a local network infrastructure of the devices). 

> **Note**  
> Application catalogs and marketplaces are out of scope of the Margo specification. The exact requirements of the marketing material shall be defined by the application marketplace beyond outlined mandatory content.

The [deployment profiles](../../specification/application-package/application-description.md#deploymentprofile-attributes) specified in the [Application Description](../../specification/application-package/application-description.md) SHALL be defined as Helm Chart components AND/OR [Compose Archive](../../personas-and-definitions/technical-lexicon.md#compose-archive) components. These components will be deployed as workloads on the edge devices:

- To target devices, which deploy workloads using Kubernetes, components must be defined as Helm charts using [Helm (version 3)](https://helm.sh/docs/topics/charts/).
- To target devices, which deploy workloads using [Compose](https://www.compose-spec.io/), components must be packaged as [Compose Archives](../../personas-and-definitions/technical-lexicon.md#compose-archive), i.e., a tarball file containing the `compose.yaml` file and any additional artifacts referenced by the Compose file (e.g., configuration files, environment variable files, etc.). Margo recommends to digitally sign this package and to specify the location of the public key in the `ApplicationDescription` (see `keyLocation` [here](../../specification/application-package/application-description.md#componentproperties-attributes)). When digitally signing the package PGP encryption MUST be used.

> **Investigation Needed**: Question: do we need to specify the location of a SHA256 hash for the Compose Archive also (similar to the PGP key) in the ApplicationDescription? 
> We will also discuss how we should handle secure container registries that require a username and password.
>
> **Investigation Needed**: We need to determine what impact, if any, using 3rd party helm charts has on being Margo compliant.
>
> **Investigation Needed**: Missing in the current specification are ways to define dependencies (e.g., application dependencies) as well as required infrastructure services such as storage, message queues/bus, reverse proxy, or authentication/authorization/accounting.

If either one cannot be implemented it MAY be omitted but Margo RECOMMENDS defining [deployment profiles](../../specification/application-package/application-description.md#deploymentprofile-attributes) as both Helm chart **AND** Compose components to strengthen interoperability and applicability.

> **Note**
> A device running the application will only install the application using either the Compose Archives or the Helm Charts, but not both.

## Relevant Links
Please follow the subsequent link to view the technical reference of the `ApplicationDescription` format:

- [Application Description](../../specification/application-package/application-description.md)
