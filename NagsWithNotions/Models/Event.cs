using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace NagsWithNotions.Models  // Adjust the namespace as needed
{
    public class Event
    {
        // You can use [Key] if you have a custom primary key
        public int Id { get; set; }  // Assuming you want an auto-generated ID

        [Required]
        [StringLength(200)]
        public string Name { get; set; }

        [StringLength(1024)]
        public string ImageUrl { get; set; }

        [NotMapped] // This indicates that this property is not mapped to a database column
        public byte[] Image { get; set; }  // Use byte array for image

        [StringLength(1024)]
        public string Description { get; set; }

        public DateTime? StartDate { get; set; }  // Nullable DateTime for optional date

        // Override ToString method
        public override string ToString()
        {
            return Name; // Equivalent to __str__ in Django
        }
    }
}
