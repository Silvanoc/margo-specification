# Application Registry

The Margo specification differentiates 4 kinds of registries: *Application Registries*, *Component Registries*, and *Container Registries* as well as *Marketplaces*.

1. An **Application Registry** hosts Application Packages that define through their [Application Description](../../specification/application-package/application-description.md) the application as one or multiple [Components](../../personas-and-definitions/technical-lexicon.md#component).
2. A **Component Registry** hosts the [Components](../../personas-and-definitions/technical-lexicon.md#component) (which are deployable as *workloads*) and are provided  as **Helm Charts** or **Compose Archives**.
3. A **Container Registry** hosts container images referenced by those Components.
4. A **Marketplace** lists applications to advertise them and enable purchasing for end users.

Out of these 4 registries, **only the Application Registry interface is in scope** of the Margo specification and its API definition can be found [here](../../specification/application-package/application-registry.md).  

The diagram below illustrates these functionalities and relationships of registries within Margo.

```mermaid
flowchart
   A[WFM, or internal Application Catalog] -- Application Descriptions link to --> B[Component Registry] 
   C[Application Registry] -- Application Descriptions link to --> B
   B -- hosted Components links to --> D[Container Registry]
   A -->|pulls Application Package | C
   F[App Developer] -->|uploads Application Package to| C
   G["Marketplace"] -- points to Application Package --> C
   C -->|hosts 0..*| E@{ shape: docs, label: "Application Packages"} 
   C -->|validates token| H[Authentication Service] 
   A -->|requests token| H
   style H stroke-dasharray: 3 6

   style B fill:#ABC
   style C fill:#ABC
   style D fill:#ABC
   style G fill:#ABC
```

As shown in the figure above, an `Application Developer` uploads an [Application package](application-package.md) to an Application Registry. From there, it is available to a `Workload Fleet Manager` (WFM).
The WFM acts as a client to pull an [Application Package](application-package.md) from the Application Registry. It would then list this Application Package on its UI (e.g., an internal `Application Catalog`) to enable the usage on its managed devices.

An `Authentication Service` manages access control for the Application Registry. The WFM requests a token from the Authentication Service to include in the requests to the Application Registry. The received token is then validated by the Application Registry through interaction with the Authentication Service.

The Application Registry's API is compliant with the [OCI Registry API (v1.1.0)](https://github.com/opencontainers/distribution-spec/blob/v1.1.0/spec.md). A hosted Application Package is provided by listing its parts as layers in an [image manifests](https://github.com/opencontainers/image-spec/blob/v1.0.1/manifest.md) that can be requested through the API.


## Relevant Links
* The technical reference of the Application Registry API is defined [here](../../specification/application-package/application-registry.md).

* A reference implementation of the Application Registry is described [here](https://github.com/margo/app-package-definition-wg/blob/main/application-registry-example/app_registry_as_oci_registry.md) and includes sample applications and configuration for demonstration. It utilizes an open source OCI Registry and the [ORAS tool](https://oras.land/docs/) as the client.
