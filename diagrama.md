```mermaid
flowchart LR
    %% --- ESTILIZAÇÃO VISUAL ---
    classDef entidade fill:#ffffff,stroke:#222222,stroke-width:2px,color:#000000,font-weight:bold;
    classDef atributo fill:#ffffff,stroke:#444444,stroke-width:1.5px,color:#222222;
    classDef atributoPK fill:#ffffff,stroke:#000000,stroke-width:2.5px,color:#000000,font-weight:bold;
    classDef atributoDerivado fill:#ffffff,stroke:#444444,stroke-width:1.5px,stroke-dasharray: 4 4,color:#555555;
    classDef relacao fill:#ffffff,stroke:#222222,stroke-width:1.5px,color:#000000,font-weight:bold;
    classDef disjuncao fill:#ffffff,stroke:#222222,stroke-width:1.5px,color:#000000,font-weight:bold;

    %% --- ENTIDADES ---
    MESA[MESA]:::entidade
    ATENDIMENTO[ATENDIMENTO]:::entidade
    PEDIDO[PEDIDO]:::entidade
    PAGAMENTO[PAGAMENTO]:::entidade
    PRODUTO[PRODUTO]:::entidade
    SUCO[SUCO]:::entidade
    SANDUICHE[SANDUICHE]:::entidade
    SALADA[SALADA DE FRUTAS]:::entidade

    %% --- RELACIONAMENTOS ---
    R_POSSUI{ POSSUI }:::relacao
    R_CONTEM{ CONTÉM }:::relacao
    R_RECEBE{ RECEBE }:::relacao
    R_INCLUI{ INCLUI }:::relacao
    D{ D }:::disjuncao

    %% --- ATRIBUTOS MESA ---
    A_m_num([numero]):::atributoPK
    A_m_ocup([ocupada]):::atributo
    MESA --- A_m_num
    MESA --- A_m_ocup

    %% --- ATRIBUTOS ATENDIMENTO ---
    A_at_ativo([ativo]):::atributo
    A_at_tot([total]):::atributoDerivado
    A_at_pago([total_pago]):::atributoDerivado
    A_at_saldo([saldo]):::atributoDerivado
    ATENDIMENTO --- A_at_ativo
    ATENDIMENTO --- A_at_tot
    ATENDIMENTO --- A_at_pago
    ATENDIMENTO --- A_at_saldo

    %% --- ATRIBUTOS PEDIDO ---
    A_ped_qtd([quantidade]):::atributo
    A_ped_sub([valor_total]):::atributoDerivado
    PEDIDO --- A_ped_qtd
    PEDIDO --- A_ped_sub

    %% --- ATRIBUTOS PAGAMENTO ---
    A_pag_val([valor]):::atributo
    PAGAMENTO --- A_pag_val

    %% --- ATRIBUTOS PRODUTO E SUBCLASSES ---
    A_pr_cod([codigo]):::atributoPK
    A_pr_nom([nome]):::atributo
    A_pr_pre([preco]):::atributo
    PRODUTO --- A_pr_cod
    PRODUTO --- A_pr_nom
    PRODUTO --- A_pr_pre

    SUCO --- A_s_tam([tamanho]):::atributo
    SANDUICHE --- A_sa_pao([pao]):::atributo
    SALADA --- A_sf_adi([adicional]):::atributo

    %% --- CADEIA PRINCIPAL E CARDINALIDADES ---
    MESA ---|1, 1| R_POSSUI
    R_POSSUI ---|0, N| ATENDIMENTO

    ATENDIMENTO ---|1, 1| R_CONTEM
    R_CONTEM ---|0, N| PEDIDO

    ATENDIMENTO ---|1, 1| R_RECEBE
    R_RECEBE ---|0, N| PAGAMENTO

    PEDIDO ---|0, N| R_INCLUI
    R_INCLUI ---|1, 1| PRODUTO

    %% --- HERANÇA (D) ---
    PRODUTO --- D
    D --- SUCO
    D --- SANDUICHE
    D --- SALADA
```
