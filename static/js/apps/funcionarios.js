$(".remove_funcionario").on("click", function () {
  let id_funcionario = $(this).attr("id");

  Swal.fire({
    title: "Deseja remover esse Perfil?",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Sim",
    cancelButtonText: "Não",
    reverseButtons: true,
  }).then((result) => {
    if (result.isConfirmed) {
      $.ajax({
        type: "POST",
        url: "/funcionarios/delete",
        data: { id_funcionario: id_funcionario },
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
