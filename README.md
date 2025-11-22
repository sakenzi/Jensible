# Схема базы данных (ERD)

Ниже представлена упрощённая ER-диаграмма сущностей и связи между ними.

```mermaid
erDiagram
    USERS ||--o{ PIPELINES : creates
    USERS {
        int id PK
        string email
        string password
        string role
    }

    PIPELINES ||--o{ PIPELINE_RUNS : has
    PIPELINES {
        int id PK
        string name
        json config
    }

    PIPELINE_RUNS {
        int id PK
        int pipeline_id FK
        string status
        text logs
    }

    DOCKER_HOSTS ||--o{ DOCKER_CONTAINERS : "hosts"
    DOCKER_HOSTS {
        int id PK
        string name
        string url
        string token
    }

    DOCKER_CONTAINERS {
        int id PK
        int host_id FK
        string name
        string image
    }

    K8S_CLUSTERS ||--o{ K8S_DEPLOYMENTS : "manages"
    K8S_CLUSTERS {
        int id PK
        string name
        text kubeconfig
        string status
    }

    K8S_DEPLOYMENTS {
        int id PK
        int cluster_id FK
        string name
        text yaml
    }

    ANSIBLE_PLAYBOOKS ||--o{ ANSIBLE_RUNS : executes
    ANSIBLE_PLAYBOOKS {
        int id PK
        string name
        string path
        int inventory_id FK
    }

    ANSIBLE_RUNS {
        int id PK
        int playbook_id FK
        string status
        text log
    }

    LOGS {
        int id PK
        string type
        int reference_id
        text text
    }

    INTEGRATIONS {
        int id PK
        string type
        json config
    }

