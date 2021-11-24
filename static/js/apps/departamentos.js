$(".remover_departamento").on("click", function () {
    let id_departamento = $(this).attr("id");
  
    Swal.fire({
      title: "Deseja remover esse Departamento?",
      icon: "question",
      showCancelButton: true,
      confirmButtonText: "Sim",
      cancelButtonText: "Não",
      reverseButtons: true,
    }).then((result) => {
      if (result.isConfirmed) {
        $.ajax({
          type: "POST",
          url: "/departamentos/delete",
          data: { id_departamento: id_departamento },
          success: function (data) {
            Swal.fire({
              text: data.text,
              title: data.title,
              icon: data.icon,
            }).then((okay) => {
              if (okay) {
                location.reload();
              }
            });
          },
          error: function (data) {
            Swal.fire({ text: data.text, title: data.title, icon: data.icon });
          },
        });
      }
    });
  });
  